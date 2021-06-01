#  https://codeforces.com/group/hPNKVTNJU1/contest/329955/problem/C

n=int(input())
 
matrix=[[1]*n]*n
for i in range(1,n):
    for j in range(1,n):
        matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
print(matrix[n-1][n-1])