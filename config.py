from configparser import ConfigParser
import os
filePath='D:\\mylog'
def getconf(key):
    conf=ConfigParser()
    conf.read(os.path.join(filePath,'conf.ini'))
    value=conf.get('db', 'db_pass')
    return value