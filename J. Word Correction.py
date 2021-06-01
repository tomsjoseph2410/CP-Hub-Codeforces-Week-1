# https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/J

n = int(input())
s = list(map(str, input()))
s.append("0")
vowel = ["a", "e", "i", "o", "u", "y"]
k = 1
while (k == 1):
 
 
    for i in range(len(s)):
        if s[i] in vowel and s[i + 1] in vowel:
            s.pop(i+1)
            k=1
            break
        k = 0
s.pop()
print("".join(s))