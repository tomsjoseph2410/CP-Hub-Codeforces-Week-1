# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/L

n=int(input())
s=list(map(int,input().split()))
s=list(set(s))
s.sort()
if len(s)>1:
    print(s[1])
else:
    print("NO")