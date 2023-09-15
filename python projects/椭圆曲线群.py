def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def modinv(x, p):
    if gcd(x, p) == 1:
        count = 0
        for i in range(1, p):
            if gcd(i, p) == 1:
                count += 1
        ans = x ** (count - 1) % p
        return ans


def ifprimary(x):  # 判断素数
    for i in range(2, x - 1):
        if x % i == 0:
            return 0
    return 1


def have_root(a, p):  # 判断是否有根
    if a ** ((p - 1) / 2) % p == 1:
        return 1
    else:
        return 0


def mod_2_root(x, p):  # 求模平方根
    t = 0
    s = p - 1
    while s % 2 == 0:
        s = s // 2
        t = t + 1
    if t == 1:
        ret = x ** ((s + 1) // 2) % p
        return ret, p - ret
    elif t >= 2:
        x_ = x ** (p - 2) % p
        n = 1
        while have_root(n, p):
            n = n + 1
        b = n ** s % p
        ret = x ** ((s + 1) // 2) % p
        t_ = 0
        while t - 1 > 0:
            if (x_ * ret * ret) ** (2 ** (t - 2)) % p == 1:
                pass
            else:
                ret = ret * (b ** (2 ** t_)) % p
            t = t - 1
            t_ = t_ + 1
        return ret, p - ret
    else:
        return -2, -2


def group(a=1, b=6, p=11):  # 构造群
    if ifprimary(p) == 0:
        print('error: p not primary')
        raise ValueError('p必须是素数')
        return
    z = ['O(无穷远点)']
    for i in range(p):
        if have_root(i ** 3 + a * i + b, p):
            z.append((i, mod_2_root(i ** 3 + a * i + b, p)[1]))
            z.append((i, mod_2_root(i ** 3 + a * i + b, p)[0]))
    return z


def add(x_p, y_p, x_q, y_q, a=1, b=6, p=11):
    g = group(a, b, p)
    P = (x_p, y_p)
    Q = (x_q, y_q)
    if P not in g:
        print('error: not in group')
        raise ValueError('P和Q必须在群内')
    elif Q not in g:
        print('error: not in group')
        raise ValueError('P和Q必须在群内')

    if x_p == x_q:
        delta = (((x_p ** 2) * 3 + a) * modinv(y_p * 2, p)) % p
    else:
        delta = ((y_p - y_q) * modinv((x_p - x_q), p)) % p
    xr = (delta ** 2 - x_p - x_q) % p
    yr = (delta * (x_p - xr) - y_p) % p
    return xr, yr


a = int(input('a= '))
b = int(input('b= '))
p = int(input('p= '))
print(f'椭圆方程有 y^2=x^3+{a}*x+{b} mod {p} 的有限群为：\n{group(a, b, p)}')
xp = int(input('xP= '))
yp = int(input('yP= '))
xq = int(input('xQ= '))
yq = int(input('yQ= '))
print('ANS:\nadd(P,Q)= ', add(xp, yp, xq, yq, a, b, p))
