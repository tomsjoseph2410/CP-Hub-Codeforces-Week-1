# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/N

n=int(input())
w=[]
 
for i in range(1,(n//2) +5):
    if n%i==0:
        w.append(i)
w.append(n)
w.sort(reverse=True)
k=0
for i in w:
    for k in range(20):
        if i == ((2 ** k) - 1) * (2 ** (k - 1)):
            print(i)
            k=1
            break
    if k==1:
        break