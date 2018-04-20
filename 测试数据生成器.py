# -*- coding: utf-8 -
import random
f1=open("D:\\can\\data1.txt","w",encoding="utf-8")
i=10000000
while(1):
    s=random.randint(0,1000)
    f1.write(str(s)+" "+"\n")
    i-=1
    if(not i):
        break
f1.close()