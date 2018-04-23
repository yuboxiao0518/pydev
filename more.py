def more(text,numlines=15):
    lines=text.splitlines()
    while lines:
        chunk=lines[:numlines]
        lines=lines[numlines:]
        for line in chunk:print(line)
        if lines and input('more?') not in ['y','Y']:break

if __name__=='__main__':
    import os
    path='D:\\mylog'
    more(open(os.path.join(path,'log.csv')).read(),10)