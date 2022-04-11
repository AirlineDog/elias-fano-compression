import hashlib
import math

# read numbers
nums = []
with open("example_3.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        nums.append(int(line.strip()))

l = int(math.log2(nums[-1]/len(nums)))
print("l = ", + str(l))

L = []
Utemp = []
for n in nums:
    L.append(n % (1 << l))
    Utemp.append(n >> l)
   
U = []
U.append(Utemp[0])
for i in range(1, len(Utemp)):
    U.append(Utemp[i] - Utemp[i-1])

L_bit_sequence = 0
for number in L:
    L_bit_sequence = (L_bit_sequence << l) | number

a = len(L) * l # number of bits in L
b = a % 8 # number of bits in L that are in the last byte
# number of zeros needed to fill the last byte
if b > 0:
    after = 8 - b
else: 
    after = 0 
n = a + after # number of bits in L

L = bytearray()
for i in range(n//8):
    if n//8 -1 == i:
        byte = L_bit_sequence << after & 0xFF
    else:
        byte = L_bit_sequence >> (n - 8*(i+1) - after) & 0xFF
    L.append(byte)

# print L bytes
print("L")
for i in L:
    print(f"{i:08b}")

U_bit_sequence = 1
for bit in U:
    U_bit_sequence = (U_bit_sequence << bit + 1) | 1

a = len(U) + sum(U) # number of bits in U
b = a % 8 # number of bits in U that are in the last byte
# number of zeros needed to fill the last byte
if b > 0:
    after = 8 - b
else: 
    after = 0 
n = a + after # number of bits in U
U = bytearray()
for i in range(n//8):
    if n//8 -1 == i:
        byte = U_bit_sequence << after & 0xFF
    else:
        byte = U_bit_sequence >> (n - 8*(i+1) - after) & 0xFF
    U.append(byte)

# print U bytes
print("U")
for i in U:
    print(f"{i:08b}")

# calculate hash value
m = hashlib.sha256()
m.update(L)
m.update(U)
print(m.hexdigest())
