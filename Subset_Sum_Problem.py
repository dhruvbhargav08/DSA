#This is from Geeks for Geeks.Question link at last
# Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 
#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, summ):
        # code here 
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
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1