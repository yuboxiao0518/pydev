import threading
import os
import time

# 用户名
user = 'ybx'
# 密码
passwd = 'ybx'
# 备份保存路径
savepath = 'D:\\app\\yubx\\home\\oracle\\orcl_bak\\'
# 要备份的表
tables = ' tables=AC_MENU,AC_OPERATOR'
full=' full=y'
# 备份周期
circle = 2.0

# 备份命令
global bak_command

bak_command = 'exp ' + user + '/' + passwd + ' file=' + savepath

def orclBak():
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    command = bak_command + now + '.dmp' + full
    print(command)
    if os.system(command) == 0:
        print("备份成功")
    else:
        print("备份失败")


if __name__ == '__main__':
    orclBak()