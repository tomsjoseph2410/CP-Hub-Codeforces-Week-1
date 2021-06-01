# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/K
p, n = list(map(int, input().split()))
a = [0] * p
 
m=1
for i in range(n):
    k=int(input())
    mod=k%p
 
    if a[mod]!=0:
        print(i+1)
        m=0
        break
 
    else:
        a[mod]=1
 
if m==1:
    print(-1)