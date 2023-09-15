def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def mod_inv(x, n):
    if gcd(x, n) == 1:
        count = 0
        for i in range(1, n):
            if gcd(i, n) == 1:
                count += 1
        ans = x ** (count - 1) % n
        return ans


p = int(input('p= '))
a = int(input('a= '))
if gcd(a, p) != 1:
    print('wrong!')
else:
    print(mod_inv(a, p))
