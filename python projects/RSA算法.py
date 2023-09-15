from random import randrange


def isprime(n):
    for j in range(1, n):
        if n % j == 0:
            return False
    return True


primes = [2, 3]
for i in range(primes[-1] + 1, 235):
    for p in primes:
        if i % p:
            continue
        else:
            break
    else:
        primes.append(i)


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


def get_prime(n):
    assert n > 1
    while True:
        while True:
            c = randrange(2 ** (n - 1) + 1, 2 ** n, 2)
            for divisor in primes:
                if c % divisor == 0 and divisor ** 2 <= c:
                    break
            pp = c
            break
        if mr_check(pp):
            return pp


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a // gcd(a, b) * b


def ext_gcd(a, b):
    old_s, s = 1, 0
    old_t, t = 0, 1
    while b:
        q = a // b
        s, old_s = old_s - q * s, s
        t, old_t = old_t - q * t, t
        a, b = b, a % b
    return a, old_s, old_t


def mod_inv(e, n):
    g, d, y = ext_gcd(e, n)
    assert g == 1
    if d < 0:
        d += n
    return d


def uint_from_bytes(x: bytes) -> int:
    return int.from_bytes(x, 'big')


def uint_to_bytes(x: int) -> bytes:
    if x == 0:
        return bytes(1)
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def RSA_keys(key_length=512, exponent=3):
    e = exponent
    t = 0
    p = 2
    q = 2
    while gcd(e, t) != 1:
        p = get_prime(key_length // 2)
        q = get_prime(key_length // 2)
        t = lcm(p - 1, q - 1)
    n = p * q
    d = mod_inv(e, t)
    return {'n': n, 'd': d, 'e': e}


def encrypt(binary_data: bytes, key):
    int_data = uint_from_bytes(binary_data)
    return pow(int_data, key['e'], key['n'])


def decrypt(encrypted_int_data: int, key):
    int_data = pow(encrypted_int_data, key['d'], key['n'])
    return uint_to_bytes(int_data)


keys = RSA_keys()  # 生成密钥
msg = b'Gu Wencong'  # 明文
ctxt = encrypt(msg, keys)  # 密文
m = decrypt(ctxt, keys)  # 解密
print(ctxt)
print(m)
