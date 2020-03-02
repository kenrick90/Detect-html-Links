import re

n=int(input())
l = []
for i in range(n):
    htmlline=input()
    text=re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>',htmlline)
    if (len(text)>1):
        l.append(text)
#
for i in range(len(l)):
    for k in range(len(l[i])):
        print(l[i][k][0]+','+l[i][k][1])