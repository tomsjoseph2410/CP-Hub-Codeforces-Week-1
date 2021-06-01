# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/F

n=int(input())
s=list(map(int,input().split()))
count=0
untreated=0
for i in range(len(s)):
    if s[i]>0:
        count+=s[i]
 
    if s[i]<0 and count<1 :
        untreated+=1
 
    if s[i]<0 and count>0:
        count-=1
print(untreated)
 