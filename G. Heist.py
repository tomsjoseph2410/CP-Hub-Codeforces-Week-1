# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/G

n=int(input())
s=list(map(int,input().split()))
s.sort()
count=0
 
for i in range(n-1):
    count+= s[i+1]-s[i]-1
print(count)