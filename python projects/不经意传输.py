import random

# 公共参数
g = 5

# 发送者Alice
x0 = 7
x1 = 9
C = random.randint(1, 16)
a = random.randint(1, 16)

# 传输参数C
CBob = C

# 接收者Bob
r = 0
k = random.randint(1, 8)
pk = [1, 1]
pk[r] = g ** k
pk[1 - r] = CBob / (g ** k)

# 传输参数pk0
pk0 = pk[0]

# 发送者Alice
pk1 = (C / pk0) ** a
E0 = (g ** a, hash(pk0 ** a) ^ x0)
E1 = (g ** a, hash(pk1 ** a) ^ x1)

# 传输参数E0，E1
EBob = [E0, E1]

# 接收者Bob
hash_pkr = hash(EBob[0][0] ** k)
xr = EBob[r][1] ^ hash_pkr

print(xr)
