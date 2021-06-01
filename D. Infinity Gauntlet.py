# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/D

n=int(input())
w=[]
s=["purple", "green", "blue", "orange", "red", "yellow"]
s_dict={
    "purple":"Power",
    "green":"Time",
    "blue":"Space",
    "orange":"Soul",
    "red":"Reality",
    "yellow":"Mind"
}
 
for i in range(n):
    k=input()
    s.remove(k)
print(6-n)
for i in range(len(s)):
    print(s_dict[s[i]])