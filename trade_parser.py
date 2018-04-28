import pandas as pd
import os

path = 'D:\\GIT'


def parse():
    file = os.path.join(path, 'jpmtradefile_20180426091936_gwdf.csv')
    tradedata = pd.read_csv(file, sep=',', header=None)
    ji, ou = [], []
    for i in range(0, 721):
        if i % 2 == 0:
            ou.append(i)
        else:
            ji.append(i)
    dantrade = tradedata.ix[ji, 0:5]
    dantrade.columns = ['a', 'b', 'c', 'd', 'e', 'f']
    shtrade = tradedata.ix[ou, 0:5]
    shtrade.columns=['q', 'w', 'r', 't', 'y', 'u']
    trade=pd.merge(dantrade, shtrade, left_on='d',right_on='t')
    print(trade)


if __name__ == '__main__':
    parse()
