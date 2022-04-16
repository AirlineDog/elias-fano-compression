import hashlib
import math
import sys

# read numbers
nums = []
with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    for line in lines:
        nums.append(int(line.strip()))

l = int(math.log2(nums[-1]/len(nums)))
print("l = " + str(l))

last_bits = bytearray()
first_bits = bytearray()
for n in nums:
    last_bits.append(n % (1 << l))
    first_bits.append(n >> l)

U_diff = bytearray()
U_diff.append(first_bits[0])
for i in range(1, len(first_bits)):
    U_diff.append(first_bits[i] - first_bits[i-1])

L = bytearray()
x = 8 - l
L.append(0)
i = 0
for number in last_bits:
    if x > 0:
        L[i] = L[i] | (number << x)
        x -= l
    elif x < 0:
        L[i] = L[i] | (number >> -x)
        i += 1
        L.append(0)
        L[i] = L[i] | ((number << (8 + x)) & 0xFF)
        x = 8 + x - l
    else:
        L[i] = L[i] | (number << x)
        if i < math.ceil(l * len(last_bits) / 8) - 1:
            i += 1
            L.append(0)
            x = 8 - l

# print L bytes
print("L")
for i in L:
    print(f"{i:08b}")

U = bytearray()
U.append(0)
i = 0
x = -1
for bit in U_diff:
    x += bit + 1
    if x < 8:
        U[i] = U[i] | (128 >> x)
    else:
        U.append(0)
        i += 1
        x = x - 8
        U[i] = U[i] | (128 >> x)

print("U")
for i in U:
    print(f"{i:08b}")

# calculate hash value
m = hashlib.sha256()
m.update(L)
m.update(U)
print(m.hexdigest())
