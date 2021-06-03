# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/O

n=int(input())
w=[]
c=0
for i in range(n):
    a,b=list(input().split())
    if (a,b) not in w:
        c+=1
        w.append((a,b))
print(c)
 
 