# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/I

r,c=list(map(int,input().split()))
e=[]
count=0
count2=0
for i in range(r):
    w=list(input())
    e.append(w)
 
 
for i in range(c):
    straw = 0
    count+=count2
 
 
    count2=0
 
    for j in range(r):
        if e[j][i]=="S":
            straw+=1
        else:
            e[j][i]="1"
            count2+=1
 
 
    if straw>0:
        for j in range(r):
            if e[j][i] =="1":
                e[j][i]="."
        count2=0
 
 
count+=count2
 
count3=0
for i in range(r):
    straw = 0
    count+=count3
 
    count3=0
 
    for j in range(c):
        if e[i][j] == "S":
            straw += 1
        else:
            if e[i][j]!="1":
                count3+=1
                e[i][j] = "1"
 
 
    if straw > 0:
        for j in range(c):
            if e[i][j] != "S":
                e[i][j] = "."
        count3=0
count+=count3
 
print(count)