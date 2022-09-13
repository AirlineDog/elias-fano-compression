# elias-fano-compression
Let's say we have a sorted list of positive integers that we want to compress:

```[5, 8, 11, 20, 33]```

This list has `n = 5` integers with `m = 33` being  the maximum.
We are going to use two bytearrays to compress those integers.
The first one *L* contains the last `l = ⌊lg(m/n)⌋ = ⌊lg(33/5)⌋ = 2 bits` of every integer in the list and has a size of `n⌊lg(m/n)⌋`

![image](https://user-images.githubusercontent.com/72792044/189884197-fdd5a766-94fa-4406-94a5-0410af03c212.png)

The second bytearray *U* will be used to represent the remaining bits of every integer. The number of those bits is `u = ⌈lgm⌉ - l = ⌈lg33⌉ - 2 = 4 bits`

![image](https://user-images.githubusercontent.com/72792044/189884883-3ff0d109-efbe-492b-a08e-d03ed8fcc7db.png)


But we are not going to store them exactly this way. Instead of the first bits we will use the difference with the previous one. That is because the difference b - a between two positive  integers a and b with a <= b is always less than their original values and therefore we save space.

![image](https://user-images.githubusercontent.com/72792044/189891813-2fb9ccab-543b-40ca-b610-8b2f44b35320.png)

Those differences will be stored in a unary numbering system. For  example the number 5 would be represented as five zeros followed by one as a separator.

![image](https://user-images.githubusercontent.com/72792044/189892211-b8c33975-5edf-491d-a7d4-49292500c730.png)

There is also a different way to construct *U* which will for sure contain 1 *n* times as we need a 1 for every integer separator. Concerning the number of zeros, this will not be more than the number of the *u* first bits of the maximum number *m*. So, the number of zeros will not be greater than `⌊m/2^l⌋`. In total *U* will contain `n + ⌊m/2^l⌋` bits. We construct *U* by initializing every bit with zeros. For the integer in place *i* of the initial list, if the value of the first *u* bits is *k*, we set the *i + k* bit to 1.

The final representation of the initial list is the two bytearrays *L* and *U*
Now let's see how much space we saved with the compression:

The initial list needs `n⌈lgm⌉` bits if every integer is stored with the same number of bits as the maximum *m*  
*L* needs `n⌊lg(m/n)⌋` bits   
*U* needs `⌊m/2^l⌋` bits  

We save : `n⌈lgm⌉ - n⌊lg(m/n)⌋ - ⌊m/2^l⌋ = n*lgm - n*lgm + n*lgn - m/2^l = n*lgn - m/2^l` bits
