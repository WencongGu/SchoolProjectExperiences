import random
import numpy as np
import pylab as pl


def generate_sets(d, n=800):
    """
    生成两个不相交的、线性可分的有限集合
    :param d: 数据维度
    :param n: 集合的元素个数上限
    :return: 返回一个包含两个集合的数组
    """
    # 生成随机的分类超平面
    b = random.randint(1, 10)
    w = np.array([random.randint(1, 50) for _ in range(d)] + [b])
    # 生成集合元素个数
    n_a = random.randint(0, n)
    na = 0
    n_b = random.randint(0, n)
    nb = 0
    # 分别生成集合
    set1 = []
    set2 = []
    while na <= n_a:
        x = np.array([random.randint(-50, 50) for _ in range(d)] + [-1])
        if x.dot(w) > 300:
            set1.append(x)
            na = na + 1
    while nb <= n_b:
        x = np.array([random.randint(-50, 50) for _ in range(d)] + [-1])
        if x.dot(w) < -300:
            set2.append(x)
            nb = nb + 1
    A = np.array(set1)
    B = np.array(set2)
    return A, B, w, n_a, n_b


def train(X, learning_rate=2.0):
    """
    训练一个有限型感知器，并返回权重值
    :param X: 训练数据，每行表示一个样本，每列表示一个特征
    :param learning_rate: 学习率，默认值为 1.0
    :return: 返回一个一维的 NumPy 数组，表示权重值
    """
    n, d = X.shape
    w = learning_rate * X[random.randint(0, n - 1)]
    k = 0
    while True:
        mistakes = 0
        for i in range(n):
            if X[i].dot(w) <= 0:
                w = w + learning_rate * X[i]
                mistakes = mistakes + 1
        if mistakes == 0:
            break
        k = k + 1
    return w, k


A, B, w, n_a, n_b = generate_sets(2)
pl.xlabel("x")
pl.ylabel("y")
pl.scatter(A[:, 0], A[:, 1], s=20, c='r', marker='*')
pl.scatter(B[:, 0], B[:, 1], s=10, c='b', marker='o')
X = np.append(A, B, axis=0)
W, k = train(X)
ax = np.arange(-50, 50, 1)  # 决策面横坐标
ay = (w[2] - w[0] * ax) / w[1]  # 决策面纵坐标
pl.plot(ax, ay, label="$w_0 x+w_1 y-w_2=0$", color="g", linewidth=2)
pl.xlim(-50, 50, 1)
pl.ylim(-50, 50, 1)
pl.show()

print('A中元素个数：', n_a)
print('B中元素个数：', n_b)
print('迭代次数：', k)
print('感知器模型：', w[0], "* x +", w[1], '* y -', w[2], '= 0')
