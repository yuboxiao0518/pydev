from configparser import ConfigParser
import os
filePath = 'D:\\mylog'


def get(typ, key):
    conf = ConfigParser()
    conf.read(os.path.join(os.getcwd()+'\config','conf.ini'))
    value = conf.get(typ, key)
    return value

if __name__ == '__main__':
    print(get('path','config_path'))