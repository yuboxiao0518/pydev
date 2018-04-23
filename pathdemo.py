import os
import dao
import time
path='D:\\mylog'
filename = 'page_list_'+str(time.strftime("%Y%m%d"))+'.txt'
output = open(os.path.join(path,filename),'w')
for line in dao.getData():
    print(line)
    output.write(str(line)+'\n')
output.close()
