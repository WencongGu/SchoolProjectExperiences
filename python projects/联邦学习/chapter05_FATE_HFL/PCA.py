# 主成分分析，针对其他文件可能需要。

import numpy as np


def pca_mat(data, k, epsilon0):
    tran_data = data.transpose()
    ar = np.array(data)
    br = np.array(tran_data)
    S = np.dot(br, ar)
    S = S / (ar.shape[0] - 1)
    eigval, eigvect = np.linalg.eig(S)
    p = []
    for i in range(eigvect.shape[0]):
        p.append(list(eigvect[i, :]))
        p[i].append(eigval[i])
    p.sort(key=lambda x: x[len(eigvect)], reverse=True)
    at = eigval.sum()
    sum_ = 0
    for i in range(len(eigval)):
        sum_ += p[i][len(eigval)]
        if sum_ >= epsilon0 * at:
            k = i + 1
            break
    for i in range(eigvect.shape[0]):
        p[i].pop()
    mat = np.array(p[0:k])
    return mat


def pca(data, k=5, epsilon0=0.85):
    """
    主成分分析，用以提高程序运行速度。
    :param epsilon0: 主成分列的方差贡献率为epsilon0
    :param k: 原数据变为k个主成分列，k个主成分列命名为数字0~k-1
    :param data: 数据集
    :return: 规约后的数据集
    """
    tran_data = data.transpose()
    br = np.array(tran_data)
    for i in range(k):
        data[i] = list(np.dot(pca_mat(data, k, epsilon0)[i, :], br))
    data = data.loc[:, list(range(k))]
    return data
