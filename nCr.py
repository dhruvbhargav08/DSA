# This is from Geeks for Geeks.Question link at last
# Given two integers n and r, find nCr.
# Since the answer may be very large, calculate the answer modulo 10^9+7.
#User function Template for python3

class Solution:
    def nCr(self, n, r):
        if r>n:
            return 0
        if r==n:
            return 1
        prod=1
        listt=[0]*n
        for i in range (1,n+1):
            prod*=i
            listt[i-1]=prod
        n1=listt[n-1]
        n2=listt[n-r-1]
        n3=listt[r-1]
        temp=n2*n3
        mod=1000000007
        res=n1//temp
        res=res%mod
        return res
        

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
