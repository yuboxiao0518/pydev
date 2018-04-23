import pandas as pd
import os
import config
import dao

filePath='D:\\mylog'

def parseCSV():
    log=os.path.join(filePath, 'log.csv')
    logcsv=pd.read_csv(open(log),header=0)
    logcsv=logcsv[['id','username','type','url','method','params','requestip','description','detail','oper_date']]
    logcsv=logcsv[logcsv['username']=='admin']
    #print(logcsv['description'].astype(str).apply(lambda x:x[:4]))
    #print(config.getconf(''))
    dao.getData()

parseCSV()


