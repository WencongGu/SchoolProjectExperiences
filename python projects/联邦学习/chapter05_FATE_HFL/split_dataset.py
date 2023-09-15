import pandas as pd

load_credit = pd.read_csv("creditcard.csv")
credit_dataset = load_credit.head(1000)
credit = load_credit.head(1000)
credit = (credit - credit.mean()) / (credit.std())
col_names = credit.columns.values.tolist()
columns = {}
for idx, n in enumerate(col_names):
    columns[n] = "x%d" % idx
credit = credit.rename(columns=columns)
credit['y'] = credit_dataset['Class']
credit['idx'] = range(credit.shape[0])
idx = credit['idx']
credit.drop(labels=['idx'], axis=1, inplace=True)
credit.insert(0, 'idx', idx)
credit = credit.sample(frac=1)
train = credit.iloc[:130000]
eval = credit.iloc[130000:]
creditcard_1_train = train.iloc[:65000]
creditcard_1_train.to_csv('creditcard_1_train.csv', index=False, header=True)
creditcard_2_train = train.iloc[65000:]
creditcard_2_train.to_csv('creditcard_2_train.csv', index=False, header=True)
eval.to_csv('creditcard_eval.csv', index=False, header=True)
