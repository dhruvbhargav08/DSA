#This is from Geeks for Geeks.Question link at last
# There are n stairs, a person standing at the bottom wants to reach the top. 
# The person can climb either 1 stair or 2 stairs at a time. 
# Count the number of ways, the person can reach the top (order does matter).
#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        # code here
        dp=[-1 for i in range (n+1)]
        def helper(n):
            if n==0 or n==1:
                return 1
            if dp[n]!=-1:
                return dp[n]
            dp[n]=(helper(n-1)+helper(n-2))%1000000007
            return dp[n]
        return helper(n)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1?page=1&difficulty[]=1&status[]=unsolved&category[]=Dynamic%20Programming&sortBy=submissions
