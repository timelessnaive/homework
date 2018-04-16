# -*- coding: utf-8 -
import os
import tkinter as tk

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
    if (c > 1):
        return 2
    if (c<=1 and flag!=-1):
        return 3
    elif(c<=1):
        return 1
def output(path,mode):

    re=""
    num = [0]
    num *= 10
    try:
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
        f.close()
        if (mode[0]):
            re += "共有" + str(num[0]) + "个字符\n"
        if (mode[1]):
            re += "共有" + str(num[1]) + "个单词\n"
        if (mode[2]):
            re += "共有" + str(num[2]) + "个句子\n"
        if (mode[3]):
            re += "共有" + str(num[3]) + "个空行," + str(num[4]) + "个代码行," + str(num[5]) + "个注释行\n"
        print("re", re)
        return re
    except IOError:
        te.delete(1.0, tk.END)
        error="找不到文件"
        te.insert("end", error)
    except UnicodeDecodeError:
        te.delete(1.0, tk.END)
        error="存在不支持的编码类型"
        te.insert("end", error)
def work():
    te.delete(1.0, tk.END)
    path=inp.get()
    global out
    # num[0] char; num[1] word; num[2] line;3 空行 4 代码行 5 注释行
    mode = [0]
    mode *= 10
    key = ["-c", "-w", "-l", "-a", "-s"]
    j = 0
    try:
        for i in key:
            if (path.find(i) != -1):
                mode[j] = 1
            j += 1
        path = path[sfind(path, " ") + 1:].strip()
        if (mode[4]):
            for root, dirs, files in os.walk(path):
                for fle in files:
                    f_path = root + "\\" + fle
                    key = f_path[sfind(f_path, ".") + 1:]
                    if (key == "txt" or key == "c" or key == "cpp" or key == "h"):
                        # print("output(f_path, mode)",output(f_path, mode))
                        out = f_path + "\n" + output(f_path, mode)
                        te.insert("end", out)
        else:
            out = output(path, mode)
            te.insert("end", out)
        print(out)
        out = ""
    except IndexError:
        te.delete(1.0, tk.END)
        error="请输入正确的格式"
        te.insert("end", error)
    except TypeError:
        te.delete(1.0, tk.END)
        error="存在不支持的编码类型"
        te.insert("end", error)

def clear():
    te.delete(1.0, tk.END)

out = ""
window = tk.Tk()
window.title("window")
window.geometry("500x500")

inp = tk.Entry(window)
inp.pack()

b1 = tk.Button(window,text="查询",width=15,height=2,command=work)
b1.pack()

b2=tk.Button(window,text="清除",width=15,height=2,command=clear)
b2.pack()

var=tk.StringVar()
var.set("")
te=tk.Text(window,height=20)
te.pack()


window.mainloop()