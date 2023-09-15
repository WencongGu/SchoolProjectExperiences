import numpy as np


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def modinv(x, n):
    if gcd(x, n) == 1:
        for t in range(1, n):
            if (t * n + 1) % x == 0:
                z = int((t * n + 1) / x)
                return z
    else:
        print('error!')
        return


a = np.random.randint(0, 300, size=(20, 50))
b = np.random.randint(0, 300, size=(20, 1))
# 手动输入矩阵
# r=20
# c=50
# a=[]
# for i in range(r):
#     a0=[]
#     for j in range(c):
#         a0.append(int(input(f'a[{i}][{j}]= ')))
#     a.append(a0)
# b=[]
# for i in range(r):
#     b.append(int(input(f'b[{i}]= ')))
# a=np.array(a)
# b=np.array(b)
r = len(a)
b = b.reshape((r, 1))
h0 = np.hstack((a, b))
c = len(h0[0])
p = 251
print('增广矩阵：', h0, '-' * 30, sep='\n')
for k in range(r - 1):
    for q in range(k, c):
        if h0[k][q] != 0:
            for i in range(k + 1, r):
                h0[i] = (h0[i] * h0[k][q] - h0[k] * h0[i][q]) % p
            break
        else:
            for t in range(k + 1, r):
                if h0[t][q] != 0:
                    h0[k] = h0[k] + h0[t]
                    for i in range(t, r):
                        h0[i] = (h0[i] * h0[k][q] - h0[k] * h0[i][q]) % p
                    break
            else:
                continue
            break
for k in range(r - 1, 0, -1):
    for q in range(c):
        if h0[k][q] != 0:
            for i in range(k):
                h0[i] = (h0[i] * h0[k][q] - h0[k] * h0[i][q]) % p
            break
print('阶梯状矩阵：', h0, '-' * 30, sep='\n')
m = 1
for i in range(r):
    t = 0
    for j in range(c - 1):
        t = abs(h0[i][j]) + t
    if t == 0 and b[i] != 0:
        print('无解')
        m = 0
        break
if m != 0:
    h0 = h0 % p
    print(f'在模{p}的意义下有解')
    for k in range(r):
        for i in range(c - 1):
            if h0[k][i] != 0:
                Ainv = modinv(h0[k][i], p)
                print(f'x[{i}]=', end='')
                for j in range(i + 1, c - 1):
                    if h0[k][j] != 0:
                        print(f'+{(-Ainv * h0[k][j]) % p}*x[{j}]', end='')
                print(f'+{(Ainv * h0[k][c - 1]) % p}')
                break
print(gcd(1387,101251))