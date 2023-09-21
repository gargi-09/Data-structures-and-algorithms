# Implementation of Longest Common Subsequence

def lcs_rec(X,Y,m,n):
    if m==0 or n==0:
        return 0
    if X[m-1]==Y[n-1]:
        return 1+lcs_rec(X,Y,m-1,n-1)
    else:
        return max(lcs_rec(X,Y,m-1,n),lcs_rec(X,Y,m,n-1))

def lcs_memo(X,Y,m,n):
    if m==0 or n==0:
        return 0
    if dp[m][n]!=-1:
        return dp[m][n]
    if X[m-1]==Y[n-1]:
        dp[m][n] = 1+lcs_memo(X,Y,m-1,n-1)
        return dp[m][n]
    
    dp[m][n] = max(lcs_memo(X,Y,m-1,n),lcs_memo(X,Y,m,n-1))
    return dp[m][n]

def lcs_tab(X,Y,m,n):
    dp = [[None for _ in range(n+1)] for k in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif X[i-1]==Y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

X="ACBD"
Y= "ABEF"
m = len(X)
n = len(Y)
print(lcs_rec(X,Y,m,n))
dp = [[-1 for _ in range(n+1)] for i in range(m+1)]
print(lcs_memo(X,Y,m,n))
print(lcs_tab(X,Y,m,n),-1)