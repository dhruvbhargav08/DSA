# This is from Geeks for Geeks.Question link at last
# There is a row of N walls in Geeksland. 
# The king of Geeksland ordered Alexa to color all the walls on the occasion of New Year. 
# Alexa can color each wall with one of the K colors. 
# The cost associated with coloring each wall with a particular color is represented by a 2D costs array of size N * K. 
# For example, costs[0][0] is the cost of coloring wall 0 with color 0; costs[1][2] is the cost of coloring wall 1 with color 2, and so on... 
# Find the minimum cost to color all the walls such that no two adjacent walls have the same color.
# Note: If you are not able to paint all the walls, then you should return -1.
#User function Template for python3

class Solution:
    def minCost(self, costs) -> int:
        #your code goes here
        n,k = len(costs),len(costs[0])
        dp = [[-1]*(k+1) for _ in range(n+1)]
        for i in range(k+1): dp[0][i] = 0
        for i in range(1,n+1):    
            min1 = [float('inf'),-1]
            min2 = [float('inf'),-1]
            for j in range(k):
                if min1[0] > dp[i-1][j]+costs[i-1][j]:
                    min2[0] = min1[0]
                    min2[1] = min1[1]
                    min1[0] = dp[i-1][j]+costs[i-1][j]
                    min1[1] = j
                elif min2[0] > dp[i-1][j]+costs[i-1][j]:
                    min2[0] = dp[i-1][j]+costs[i-1][j]
                    min2[1] = j
            for prev in range(k+1):
                if prev == min1[1]: dp[i][prev] = min2[0]
                else: dp[i][prev] = min1[0]
        res = dp[n][k]
        return res if res != float('inf') else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List


class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n, m = map(int, input().split())
        
        
        costs=IntMatrix().Input(n, m)
        
        obj = Solution()
        res = obj.minCost(costs)
        
        print(res)
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/9dacc32ad062be6e2ba8f6c41aad0b2b2376397d/1