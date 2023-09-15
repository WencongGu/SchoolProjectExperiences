import struct

h0 = 0x6a09e667f3bcc908
h1 = 0xbb67ae8584caa73b
h2 = 0x3c6ef372fe94f82b
h3 = 0xa54ff53a5f1d36f1
h4 = 0x510e527fade682d1
h5 = 0x9b05688c2b3e6c1f
h6 = 0x1f83d9abfb41bd6b
h7 = 0x5be0cd19137e2179
k = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc, 0x3956c25bf348b538,
     0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118, 0xd807aa98a3030242, 0x12835b0145706fbe,
     0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2, 0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235,
     0xc19bf174cf692694, 0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
     0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5, 0x983e5152ee66dfab,
     0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4, 0xc6e00bf33da88fc2, 0xd5a79147930aa725,
     0x06ca6351e003826f, 0x142929670a0e6e70, 0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed,
     0x53380d139d95b3df, 0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
     0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30, 0xd192e819d6ef5218,
     0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8, 0x19a4c116b8d2d0c8, 0x1e376c085141ab53,
     0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8, 0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373,
     0x682e6ff3d6b2b8a3, 0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
     0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b, 0xca273eceea26619c,
     0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178, 0x06f067aa72176fba, 0x0a637dc5a2c898a6,
     0x113f9804bef90dae, 0x1b710b35131c471b, 0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc,
     0x431d67c49c100d4c, 0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817
     ]


def ext(m, length=8):
    b = '0' * (length - len(m))
    b = b + m
    return b


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def my_bin(m, length=8):
    b = ''
    for i in m:
        b = b + ext(bin(ord(i))[2::], length)
    return b


def padding(m, method=512):
    if method == 512:  # sha512
        ms = 128
        size = 1024
    else:  # sha256
        ms = 64
        size = 512
    length = len(m) % size
    if length == 0:
        re = my_bin(m) + '1' + '0' * (size - 1)
        return re
    message_size = len(m) * 8
    pad = '1' + '0' * (size - message_size - 1 - ms)
    m2 = my_bin(m)
    re = m2 + pad + ext(bin(message_size)[2::], ms)
    return re


def tran_l(a, k):
    m0 = a[k::] + a[0:k]
    return m0


def s_r(m, k):
    return m[-k:] + m[:-k]


def ch(x, y, z):
    return (x & y) ^ ((~x) & z)


def ma(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)


def sigma0(x):
    return tran_l(x, 28) ^ tran_l(x, 34) ^ tran_l(x, 39)


def sigma1(x):
    return tran_l(x, 14) ^ tran_l(x, 18) ^ tran_l(x, 41)


def sig0(x):
    return tran_l(x, 1) ^ tran_l(x, 8) ^ (x >> 7)


def sig1(x):
    return tran_l(x, 19) ^ tran_l(x, 61) ^ (x >> 6)


def rightrotate(x, n):
    return x >> n


def ff(h, m):
    w = []
    for i in range(16):
        w.append(m[64 * i:64 * (i + 1)])
    for i in range(16, 80):
        w.append(sig1(w[i - 2]) + w[i - 7] + sig0(w[i - 15]) + w[i - 16])
    hh = []
    for i in range(8):
        hh.append(h[i * 64:(i + 1) * 64])
    for i in range(80):
        t1 = hh[7] + ch(hh[4], hh[5], hh[6]) + sigma1(hh[4]) + w[i] + k[i]
        t2 = sigma0(hh[0]) + ma(hh[0], hh[1], hh[2])
        hh[4] = hh[3] + t1
        hh[0] = t1 + t2
    return hh[0] + hh[1] + hh[2] + hh[3] + hh[4] + hh[5] + hh[6] + hh[7]


def sha5l2(m):
    global h0, h1, h2, h3, h4, h5, h6, h7, k
    pad_m = padding(m)
    n = int(len(pad_m) / 1024)
    import hashlib as hl
    h = hl.sha512(m.encode("utf-8"))
    hh = h.hexdigest()
    mm = []
    for i in range(n):
        mm.append(pad_m[i:(1024 * (i + 1))])
    x = str(hex(h0))[2::] + str(hex(h1))[2::] + str(hex(h2))[2::] + str(hex(h3))[2::] + str(hex(h4))[2::] \
        + str(hex(h5))[2::] + str(hex(h6))[2::] + str(hex(h7))[2::]
    for i in range(n):
        h = int(x, 16)
        if n:
            h = hh
        else:
            pass
    return h


def sha512(string):
    global h0, h1, h2, h3, h4, h5, h6, h7, k
    bytes_string = string.encode()
    length = len(bytes_string) * 8
    bytes_string += b'\x80'
    bytes_string += b'\x00' * ((120 - len(bytes_string) % 128) % 128) + struct.pack('>Q', length)
    for offset in range(0, len(bytes_string), 128):
        chunk = bytes_string[offset: offset + 128]
        w = [0] * 80
        for i in range(16):
            w[i] = struct.unpack('>Q', chunk[i * 8:i * 8 + 8])[0]
        for i in range(16, 80):
            w[i] = (w[i - 16] + rightrotate(w[i - 15], 1) ^ rightrotate(w[i - 15], 8) ^ (w[i - 15] >> 7)) + (
                    w[i - 7] + (rightrotate(w[i - 2], 19) ^ rightrotate(w[i - 2], 61) ^ (
                    w[i - 2] >> 6))) & 0xffffffffffffffff
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7
        for i in range(80 - 16):
            S1 = rightrotate((rightrotate(e, 14) ^ rightrotate(e, 18) ^ rightrotate(e, 41)), 1)
            temp1 = (h + S1 + ((e & f) ^ (~e & g)) + k[i] + w[i]) & 0xffffffffffffffff
            S0 = rightrotate((rightrotate(a, 28) ^ rightrotate(a, 34) ^ rightrotate(a, 39)), 1)
            temp2 = (S0 + ((a & b) ^ (a & c) ^ (b & c))) & 0xffffffffffffffff
            a, b, c, d, e, f, g, h, w[i + 16] = temp1, a, b, c, (d + temp1) & 0xffffffffffffffff, e, f, g, temp2
            ll = sha5l2(string)
            h0 = (h0 + a) & 0xffffffffffffffff
            h1 = (h1 + b) & 0xffffffffffffffff
            h2 = (h2 + c) & 0xffffffffffffffff
            h3 = (h3 + d) & 0xffffffffffffffff
            h4 = (h4 + e) & 0xffffffffffffffff
            h5 = (h5 + f) & 0xffffffffffffffff
            h6 = (h6 + g) & 0xffffffffffffffff
            h7 = (h7 + h) & 0xffffffffffffffff
    l1 = (h7 << 128) | (h6 << 96) | (h5 << 64) | (h4 << 32) | (h3 << 16) | (h2 << 8) | h1
    lI = format(l1, 'x')
    return ll


print(sha512('abc'))
