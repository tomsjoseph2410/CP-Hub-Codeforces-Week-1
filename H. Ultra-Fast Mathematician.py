# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/H

a=list(map(int,input()))
b=list(map(int,input()))
w=[]
 
for i in range(len(a)):
    if a[i]==b[i]:
        w.append("0")
    else:
        w.append("1")
w="".join(w)
print(w)