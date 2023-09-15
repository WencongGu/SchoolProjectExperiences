import argparse, json
from sklearn.datasets import load_iris
import datetime
import os
import numpy as np
import pandas as pd
import data_operate
from server import *
from client import *
import models, datasets
import split_dataset
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBRegressor as XGBR
from sklearn.model_selection import KFold, cross_val_score as CVS, train_test_split as TTS
from sklearn.metrics import mean_squared_error as RMSE
from xgboost import plot_importance

if __name__ == '__main__':
    data = pd.read_csv('creditcard.csv')

    data.drop_duplicates()
    data.dropna()

    sns.set_style('darkgrid', {'font.sans-serif': ['SimHei', 'Arial']})
    sns.boxenplot(x='Class', y='V1', data=data)
    plt.show()

    from sklearn import datasets
    from sklearn.model_selection import train_test_split

    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)
    from sklearn.preprocessing import StandardScaler

    standardscaler = StandardScaler()
    standardscaler.fit(X_train)
    X_train_s = standardscaler.transform(X_train)
    X_test_s = standardscaler.transform(X_test)
    from sklearn.neighbors import KNeighborsClassifier

    kNN_classify = KNeighborsClassifier(6)
    kNN_classify.fit(X_train_s, y_train)
    yhat = kNN_classify.predict(X_test_s)
    print(f'准确率：{kNN_classify.score(X_test_s, y_test)}')

    csv_path_p = data_operate.File_Upset
    csv_path = data_operate.File_Train
    save_dir = 'Part_Data'
    # 执行打乱操作
    data_operate.get_label_data()
    # 对数据集进行训练集和测试集的分割
    data_operate.Tc_Part().split_csv(csv_path_p)
    # 将训练集平均分配给各用户机
    data_operate.PyCSV().split_csv(csv_path, save_dir)

    parser = argparse.ArgumentParser(description='Federated Learning')
    parser.add_argument('-c', '--conf', dest='conf')
    args = parser.parse_args()
    split_dataset.split_dataset()
    data1 = pd.read_csv('creditcard.csv')
    print(data1.head(5))
    data0 = pd.read_csv('creditcard.csv')
    param = {
        'booster': 'gbtree',
        'objective': 'multi:softmax',
        'num_class': 3,
        'gamma': 0.1,
        'max_depth': 6,
        'lambda': 2,
        'subsample': 0.7,
        'colsample_bytree': 0.7,
        'min_child_weight': 3,
        'slient': 1,
        'eta': 0.1,
        'seed': 1000,
        'nthread': 4,
    }
    with open('utils\conf.json', 'r') as f:
        conf = json.load(f)
    for i in range(5):
        f1_score = []
        roc_auc = []
        ave_f1 = 0.00
        ave_roc_auc = 0
        hi_single_len = 0
        gi_single_len = 0
        for k in range(5):  # 共进行5轮联合更新
            print(f'第{k}个客户端正在联合更新')
            client_file = 'Part_Data/Data_Trian_' + str(k + 1) + '.csv'
            t = data_operate.PyCSV()
            t.split_csv(csv_path=client_file, save_dir='Data_Check/')
            data = pd.read_csv(client_file)
            l = load_iris()
            X, y = l.data, l.target
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123457)
            plst = param.items()
            # 生成数据集格式
            data = pd.read_csv(client_file)
            X = data.iloc[:, 1:28]
            y = data['Class']
            # 将数据随机打乱，分割为训练数据集和检测数据集
            Xtrain, Xtest, Ytrain, Ytest = TTS(X, y, test_size=0.3, random_state=420)
            reg = XGBR(n_estimators=100).fit(Xtrain, Ytrain)  # 训练
            y_Pr = reg.predict(Xtest)  # 预测

            print(f'相关系数:{reg.score(Xtest, Ytest)}')  # 预测结果的评价，采用的指标为相关系数
            print(f'均方根误差:{RMSE(Ytest, reg.predict(Xtest))}')  # 计算均方根误差
            print(f'交叉检验:{CVS(reg, Xtrain, Ytrain, cv=5).mean()}')  # 进行交叉检验
        # 显示重要特征
        plot_importance(reg)
        plt.show()
