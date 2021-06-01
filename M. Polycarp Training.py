# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/M

n=int(input())
s=list(map(int,input().split()))
s.sort()
c=0
k=1
for i in range(n):
    if s[i]>=k:
        c+=1
        k+=1
print(c)
 
 