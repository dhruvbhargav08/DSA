# This is from Geeks for Geeks.Question link at last
# Given two integers n and r, find nCr.
# Since the answer may be very large, calculate the answer modulo 10^9+7.
#User function Template for python3

class Solution:
    def nCr(self, n, r):
        # code here
        def helper():
            pass
        temp=n-r
        if temp==0:
            return 1
        elif temp<0:
            return 0
        fact_n=1
        fact_r=1
        fact_temp=1
        for i in range (1,n+1):
            fact_n*=i
        for i in range (1,r+1):
            fact_r*=i
        for i in range (1,temp+1):
            fact_temp*=i
        res=fact_n//(fact_temp*fact_r)
        return int(res%((10**9+7)))
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends
# Quetion link 
# https://practice.geeksforgeeks.org/problems/ncr1019/1?page=1&difficulty[]=1&status[]=unsolved&sortBy=submissions