#This is from Geeks for Geeks.Question link at last
# You are given a matrix grid of n x  m size consisting of values 0 and 1. 
# A value of 1 means that you can enter that cell and 0 implies that entry to that cell is not allowed.
# You start at the upper-left corner of the grid (1, 1) and you have to reach the bottom-right corner (n, m) such that you can only move in the right or down direction from every cell.
# Your task is to calculate the total number of ways of reaching the target modulo (100000007).
# Note: The first (1, 1) and last cell (n, m) of the grid can also be 0
#User function Template for python3

class Solution:
    def uniquePaths(self, n, m, grid):
        # code here
        for i in range(1,n):
            if grid[i][0]==1:
               grid[i][0]=grid[i-1][0]
        for i in range(1,m):
            if grid[0][i]==1:
               grid[0][i]=grid[0][i-1]    
        for i in range(1,n):
            for j in range(1,m):
                if grid[i][j]==1:
                    a=b=0
                    if i-1>-1:
                        a=grid[i-1][j]
                    if j-1>-1:
                        b=grid[i][j-1]
                     
                    grid[i][j]=a+b    
                    grid[i][j]%=(10**9+7)
                 
        return grid[n-1][m-1] 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m=map(int,input().split())
        
        grid=[]
        for i in range(n):
            col = list(map(int,input().split()))
            grid.append(col)
        
        ob = Solution()
        print(ob.uniquePaths(n,m,grid))
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/96161dfced02d544fc70c71d09b7a616fe726085/1