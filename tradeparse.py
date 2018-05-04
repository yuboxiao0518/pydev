import pandas as pd
import pandas_datareader.data as web   # Package and modules for importing data; this code may change depending on pandas version
import datetime
import os
import fix_yahoo_finance as fix
import tushare as ts

path = 'F:\\work'


def parse():
    file = os.path.join(path, 'jpmtradefile_20180426091936_gwdf.csv')
    tradedata = pd.read_csv(file, sep=',', header=None, engine='python')
    tradedata = tradedata[[i for i in range(0, 28)]]
    with open(file, 'r') as f:
        size = len(f.readlines())
    ji = [i for i in range(0, size) if i % 2 == 0]
    ou = [i for i in range(0, size) if i % 2 != 0]
    dbl = tradedata.loc[ji, :]
    dal = tradedata.loc[ou, :]
    try:
        data = pd.merge(dal, dbl, how='left', on='3')
        print(data)
    except Exception as err:
        print(err)




def csvDao():
    start = datetime.datetime(2018, 5, 1)
    end = datetime.date.today()
    #apple=ts.get_h_data('300032',start='2018-05-01',end='2018-05-04')
    apple=ts.get_today_all()
    data=pd.DataFrame(apple)
    print(data)


if __name__ == '__main__':
    csvDao()
