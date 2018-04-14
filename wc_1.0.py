# -*- coding: utf-8 -
while(1):
    print("请输入文件路径（包括文件名及后缀）")
    mode=0
    path = input()
    #print(path)
    if(path.find("-c")!=-1):
        mode=1
    elif(path.find("-w")!=-1):
        mode=2
    elif(path.find("-l")!=-1):
        mode=3
    elif(path=="exit"):
        break
    #print(mode)
    if(mode):
        path = path[path.find(" ")+1:]
        #print(path)
    f = open(path, "r", encoding="utf-8")
    num = [0]
    num *= 5  # num[0] char; num[1] word; num[2] line;
    line = f.readline()
    while line:
            num[0] += len(line) - 1
            num[1] += len(line.split())
            num[2] += 1
            line = f.readline()
    f.close()
    if(mode==1):
        print("共有{0}个字符\n".format(num[0]))
    elif(mode==2):
        print("共有{0}个单词\n".format(num[1]))
    elif (mode == 3):
        print("共有{0}个句子\n".format(num[2]))
    else:
        print("共有{0}个字符\n共有{1}个单词\n共有{2}个句子".format(num[0], num[1], num[2]))
    print("若要退出请输入exit")
    for i in num:
        i=0
print("感谢使用")