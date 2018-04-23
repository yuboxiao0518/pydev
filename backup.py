import threading
import os
import time

# 用户名
user = 'cdb'
# 密码
passwd = 'cdb'
# 备份保存路径
savepath = 'D:\\app\\yubx\\home\\oracle\\orcl_bak\\'
# 要备份的表
tables = ' tables=APP_MENU,CAP_PARTYAUTH'
# 备份周期
circle = 2.0

# 备份命令
global bak_command

bak_command = 'exp ' + user + '/' + passwd + ' file=' + savepath


def orclBak():
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    command = bak_command + now + '.dmp' + tables
    print(command)
    if os.system(command) == 0:
        print("备份成功")
    else:
        print("备份失败")

    global t
    t = threading.Timer(circle, orclBak)
    t.start()


t = threading.Timer(circle, orclBak)
t.start()