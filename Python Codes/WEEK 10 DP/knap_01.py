#Implementation of Knapsack 0/1
def knap_01(wt,val,W,n):
    if n==0 or W==0:
        return 0
    
    if wt[n-1]>W:
        return knap_01(wt,val,W,n-1)
    
    else:
        return max(val[n-1]+knap_01(wt,val,W-wt[n-1],n-1),knap_01(wt,val,W,n-1))

def knap_dp(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if t[n][W]!=-1:
        return t[n][W]
    if wt[n-1]>W:
        t[n][W] = knap_dp(wt,val,W,n-1)
        return t[n][W]
    else:
        t[n][W] = max(val[n-1]+knap_dp(wt,val,W-wt[n-1],n-1),knap_dp(wt,val,W,n-1))
        return t[n][W]

def knap_tab(wt,val,W,n):
    knap = [[0 for _ in range(W+1)] for i in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                knap[i][w]=0
            if wt[i-1]<=w:
                knap[i][w] = max(val[i-1]+knap[i-1][w-wt[i-1]],knap[i-1][w])
            else:
                knap[i][w] = knap[i-1][w]
    return knap[n][W]

profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(profit)
print(knap_01(weight,profit,W,n))
t = [[-1 for _ in range(W+1)] for i in range(n+1)]
print(knap_dp(weight,profit,W,n))
print(knap_tab(weight,profit,W,n))