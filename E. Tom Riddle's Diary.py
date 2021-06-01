# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/E

n=int(input())
w=[]
for i in range(n):
    s=input()
    if s in w:
        print("YES")
    else:
        print("NO")
    w.append(s)