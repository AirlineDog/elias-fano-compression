import hashlib
import math
import sys

# read numbers
numbers = []
with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    for line in lines:
        numbers.append(int(line.strip()))

m = numbers[-1] # max number
l = math.floor(math.log2(m/len(numbers))) # length of binary representation

print("l =" , l)

L = bytearray()
number_of_bits_in_L = len(numbers) * l
bytes_in_L = math.ceil(number_of_bits_in_L / 8)
for i in range(bytes_in_L):
    L.append(0)

byte = 0
bits_in_byte = 0
for number in numbers:
    bits = number & ((1 << l) - 1)
    if bits_in_byte > 8 - l:
        # overflow
        L[byte] = L[byte] | (bits >> bits_in_byte - (8 - l))
        bits_in_byte = bits_in_byte - 8
        byte += 1
    L[byte] = L[byte] | (bits << (8 - l - bits_in_byte)) & 0xFF
    bits_in_byte += l

# print L bytes
print("L")
for i in L:
    print(f"{i:08b}")

U = bytearray()
number_of_bits_in_U = len(numbers) + math.floor(m/2**l)
bytes_in_U = math.ceil(number_of_bits_in_U / 8)
for i in range(bytes_in_U):
    U.append(0)

for i, number in enumerate(numbers):
    bits = number >> l
    to_be_1 = i + bits
    byte = to_be_1 // 8
    bit = to_be_1 % 8
    U[byte] = U[byte] | (1 << (7 - bit))

print("U")
for i in U:
    print(f"{i:08b}")

# calculate hash value
m = hashlib.sha256()
m.update(L)
m.update(U)
print(m.hexdigest())
