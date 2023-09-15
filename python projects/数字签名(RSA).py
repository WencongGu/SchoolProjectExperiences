import random
from random import randrange


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def quick_mod(a, b, c):
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a * a) % c
    return ans


def mr_check(n, k=20):
    assert n > 3
    if n % 2 == 0:
        return False
    s, d = 0, n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    for t in range(k):
        a = randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(s):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def quick_isprime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    s = 4
    m = pow(2, num) - 1
    for x in range(1, (num - 2) + 1):
        s = ((s * s) - 2) % m
    if s == 0:
        return True
    else:
        return False


def ext_euclid(a, m):
    if a == 0:
        return 1, 0, m
    else:
        x, y, g = ext_euclid(m % a, a)
        x, y = y, (x - (m // a) * y)
        return x, y, g


def mod_inv(a, m):
    n = ext_euclid(a, m)
    if n[1] < 0:
        return n[1] + m
    else:
        return n[1]


def get_prime(key_size):
    while True:
        num = random.randrange(2 ** (key_size - 1), 2 ** (key_size))
        if mr_check(num):
            return num


def key_Gen(p, q):
    n = p * q
    e = random.randint(1, (p - 1) * (q - 1))
    while gcd(e, (p - 1) * (q - 1)) != 1:
        e = random.randint(1, (p - 1) * (q - 1))
    d = mod_inv(e, (p - 1) * (q - 1))
    return n, e, d


def Sign(x, d, n):
    sigma = quick_mod(x, d, n)
    return sigma


def Verify(msg,sigma, e, n):
    x = (msg==quick_mod(sigma, e, n))
    return x


# 密钥生成
key_size = 512
p = get_prime(key_size)
q = get_prime(key_size)
n, e, d = key_Gen(p, q)

# 整数型消息
msg = 5646437

# 签名
sigma = Sign(msg, d, n)

# 验证
res = Verify(msg, sigma, e, n)
print("签名 :", sigma)
print("消息验证: ")
if res:
    print("签名有效")
else:
    print("签名无效")

# 伪造消息
msg_fake = random.randint(1, msg + 1)
print('-------------\n伪造消息：',msg_fake)

#私钥选取
d_fake = random.randint(1, (p - 1) * (q - 1))
print('伪造私钥：',d_fake)

#签名
sigma_fake = Sign(msg_fake, d_fake, n)

#验证
res1 = Verify(msg_fake, sigma_fake, e, n)
print('验证结果：')
if res1 == msg:
    print('未抵挡攻击')
else:
    print('签名有误，可以抵挡攻击')
