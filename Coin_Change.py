# This is from Geeks for Geeks.Question link at last
# Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum.
# Find the number of ways you can make sum by using different combinations from coins[ ].  
# Note: Assume that you have an infinite supply of each type of coin. 
#User function Template for python3

class Solution:
        
    def count(self, coins, n, Sum):
        # code here 
        dp = [[0 for i in range(Sum+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(1,Sum+1):
                if coins[i-1] <= j:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][Sum]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/coin-change2448/0