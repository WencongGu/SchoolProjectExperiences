def ext(str, l):
    z = '0' * (l - len(str))
    str0 = list(str)
    str0.insert(0, z)
    x = ''.join(str0)
    return x


L = 108
R = bin(108)[2::]
r = ext(R, 48)
k = ''
for i in 'crypto':
    k = k + str(ext(bin(ord(i))[2::], 8))
f0 = ext(bin(int(k, 2) ^ int(r, 2))[2::], 48)
p = [[16, 7, 20, 21, 29, 12, 28, 17],
     [1, 15, 23, 26, 5, 18, 31, 10],
     [2, 8, 24, 14, 32, 27, 3, 9],
     [19, 13, 30, 6, 22, 11, 4, 25]]
s = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 2, 14, 10, 0, 6, 13]]
fs = []
for i in range(8):
    x = int(f0[6 * i:6 * (i + 1)][2::], 2)
    y = int(f0[6 * i:6 * (i + 1)][0:2], 2)
    fs.append(ext(bin(s[y][x])[2::], 4))
fs = ''.join(fs)
F = ''
for i in range(len(p)):
    for j in p[i]:
        F = F + fs[j - 1]
Ri = ext(bin(int(F, 2) ^ L)[2::], 32)
Li = ext(R, 32)
print('R(i-1)=L(i-1)= ', ext(R, 32))
print('F(R,K)= ', F)
print('Ri= ', Ri)
print('Li= ', Li)
