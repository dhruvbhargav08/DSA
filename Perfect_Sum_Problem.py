#This is from Geeks for Geeks.Question link at last
# Given an array arr[] of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.
#User function Template for python3
class Solution:
	def perfectSum(self, arr, N, summ):
		# code here
            mod=1000000007
            dp=[[-1 for i in range (summ+1)]for j in range (N+1)]
            for i in range (N+1):
                for j in range (summ+1):
                    if i==0:
                        dp[i][j]=0
            def helper(arr,summ,n):
                nonlocal dp
                if n==0 and summ>0:
                    return 0
                elif n==1:
                    if summ==0:
                        if arr[0]==0:
                            return 2
                        else:
                            return 1
                    if summ>0:
                        if arr[0]==summ:
                            return 1
                        else:
                            return 0
                elif n==0 and summ==0:
                    return 1
                if dp[n][summ]!=-1:
                    return dp[n][summ]
                if arr[n-1]<=summ:
                    dp[n][summ]=helper(arr,summ-arr[n-1],n-1) + helper(arr,summ,n-1)
                else:
                    dp[n][summ]=helper(arr,summ,n-1)
                return dp[n][summ]
            return helper(arr,summ,N)%mod
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1?page=1&difficulty[]=1&status[]=unsolved&sortBy=submissions