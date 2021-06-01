# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/B

t=int(input())
for _ in range(t):
    s=list(map(str,input().split("_")))
    if s[len(s)-1][len(s[len(s)-1])-1] == "o":
        print("FILIPINO")
    elif s[len(s)-1][len(s[len(s)-1])-1] == "u":
        print("JAPANESE")
    else:
        print("KOREAN")