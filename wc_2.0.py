# -*- coding: utf-8 -
import os
#--------------------------------
def sfind(s,aim):
    i=-1
    while(s[i]!=aim):
        i-=1
    return i
def notblank(i):
    if (i != " " and i != "\t" and i!="\n"):
        return True
    return False
def lineis(line):
    # 1 空行 2 代码行 3 注释行
    flag=line.find("//")
    c=0
    if (flag != -1):
        line=line[:flag]
    for i in list(line):
        #print(i)
        if (notblank(i)):
            c += 1
    #print("ccc",c)
    if (c > 1):
        return 2
    if (c<=1 and flag!=-1):
        return 3
    elif(c<=1):
        return 1
def output(path,mode):
    num = [0]
    num *= 10
    f = open(path, "r", encoding="utf-8")
    line = f.readline()
    c = 0
    while line:
        num[lineis(line) + 2] += 1
        # print(lineis(line))
        num[0] += len(line) - 1
        num[1] += len(line.split())
        num[2] += 1  # bug
        line = f.readline()
    # print(num)
    f.close()
    # --------------------------------------------------------
    #print(mode)
    #print(num)
    if (mode[0]):
        print("共有{0}个字符".format(num[0]))
    if (mode[1]):
        print("共有{0}个单词".format(num[1]))
    if (mode[2]):
        print("共有{0}个句子".format(num[2]))
    if (mode[3]):
        print("共有{0}个空行\n共有{1}个代码行\n共有{2}个注释行".format(num[3], num[4], num[5]))

#-----------------------------------
mode = [0]
mode *= 10
# num[0] char; num[1] word; num[2] line;3 空行 4 代码行 5 注释行
key=["-c","-w","-l","-a","-s"]
#------------------------------------
while(1):
    print("请输入文件路径（包括文件名及后缀）")
    path = input()
    j=0
    for i in key:
        if(path.find(i)!=-1):
            mode[j]=1
        j += 1
    if(path == "exit"):
        break
    path=path[sfind(path," ")+1:].strip()
    if(mode[4]):
        for root, dirs, files in os.walk(path):
            for fle in files:
                f_path = root + "\\" + fle
                key=f_path[sfind(f_path,".")+1:]
                if(key=="txt"or key=="c" or key=="cpp"):
                    print(f_path)
                    output(f_path,mode)
    else:
        output(path, mode)
    print("若要退出请输入exit")
    for i in range(10):
        mode[i]=0
