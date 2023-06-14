# This is from Geeks for Geeks.Question link at last
# There are N bags with diamonds in them. 
# The i'th of these bags contains A[i] diamonds. 
# If you drop a bag with A[i] diamonds, it changes to A[i]/2 diamonds and you gain A[i] diamonds. 
# Dropping a bag takes 1 minute. 
# Find the maximum number of diamonds that you can take if you are given K minutes.
#User function Template for python3
from sortedcontainers import SortedList
class Solution:
    def maxDiamonds(self, A, N, K):
        # code here
        res=0
        A=SortedList(A)
        for i in range (K):
            value=A.pop()
            A.add(value//2)
            res+=value
        return res 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/chinky-and-diamonds3340/1