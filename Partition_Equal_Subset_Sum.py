#This is from Geeks for Geeks.Question link at last
# Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.
# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        def subset(arr,summ,n):
            dp=[[-1 for i in range (summ+1)]for j in range (N+1)]
            for i in range (N+1):
                for j in range (summ+1):
                    if i==0:
                        dp[i][j]=False
                    if j==0:
                        dp[i][j]=True
            def helper(arr,summ,n):
                nonlocal dp
                if dp[n][summ]!=-1:
                    return dp[n][summ]
                if arr[n-1]<=summ:
                    dp[n][summ]=helper(arr,summ-arr[n-1],n-1) or helper(arr,summ,n-1)
                else:
                    dp[n][summ]=helper(arr,summ,n-1)
                return dp[n][summ]
            return helper(arr,summ,N)
        summ=sum(arr)
        if summ%2:
            return 0
        return subset(arr,summ//2,N)
        
        
        


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1?page=1&difficulty[]=1&status[]=unsolved&category[]=Dynamic%20Programming&sortBy=submissions