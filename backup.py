import threading
import os
import time
import config

# 用户名
user = config.get('db','name')
# 密码
passwd = config.get('db','pwd')
# 备份保存路径
savepath = config.get('path','config_path')
# 要备份的表
tables = ' tables=AC_MENU,AC_OPERATOR'
full=' full=y'
# 备份周期
circle = 2.0

# 备份命令
global bak_command


bak_command = 'exp ' + user + '/' + passwd + ' file=' + savepath

expdp_command='expdp '+user+'/'+passwd+'@orcl directory='+savepath


def orclBak():
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    now = time.strftime('%Y-%m-%d')
    command = expdp_command+' dumpfile=full_'+now+'.dmp full=y logfile=dmuser_schema_'+now+'.log'
    print(command)
    if os.system(command) == 0:
        print("备份成功")
    else:
        print("备份失败")

    # global t
    # t = threading.Timer(circle, orclBak)
    # t.start()


# t = threading.Timer(circle, orclBak)
# t.start()
if __name__ == '__main__':
    orclBak()
