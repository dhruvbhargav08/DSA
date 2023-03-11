# This is from Geeks for Geeks.Question link at last
# Given a binary matrix (containing only 0 and 1) of order NxN. 
# All rows are sorted already, We need to find the row number with the maximum number of 1s. 
# Also, find the number of 1s in that row.
# Note:
# 1. In case of a tie, print the smaller row number.
# 2. Row number should start from 0th index.
#User function Template for python3

class Solution:
    def findMaxRow(self, mat, N):
        # Code here
        res=[0,0]
        maxx=0
        for i in range (N):
            summ=sum(mat[i])
            if summ>maxx:
                maxx=summ
                res=[i,maxx]
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat = []
        for i in range(n):
            A = [int(x) for x in input().split()]
            mat.append(A)
        ob=Solution()
        ans = []
        ans = ob.findMaxRow(mat, n)
        for i in range(2):
            print(ans[i], end =" ")
        print()
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/77e1c3e12cd148f835d53eb168d4472b2ff539fa/1