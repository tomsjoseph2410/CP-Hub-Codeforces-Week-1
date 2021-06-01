
# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/A

s=list(input())
a=list(map(str,input().split()))
a="".join(a)
if s[0] in a or s[1] in a:
    print("YES")
else:
    print("NO")