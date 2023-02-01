#This is from Geeks for Geeks.Question link at last
# There is a row of N houses, each house can be painted with one of the three colors: red, blue or green. 
# The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color. 
# Find the minimum cost to paint all houses.
# The cost of painting each house in red, blue or green colour is given in the array r[], g[] and b[] respectively.
#User function Template for python3

class Solution:
    def distinctColoring (self, N, r, g, b):
        # code here 
        dp=[[None for _ in range (3)] for _ in range (N)]
        dp[0][0]=r[0]
        dp[0][1]=g[0]
        dp[0][2]=b[0]
        for i in range (1,N):
            dp[i][0]=min(dp[i-1][1],dp[i-1][2])+r[i]
            dp[i][1]=min(dp[i-1][0],dp[i-1][2])+g[i]
            dp[i][2]=min(dp[i-1][0],dp[i-1][1])+b[i]
        return min(dp[N-1][0],dp[N-1][1],dp[N-1][2])
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        r = list(map(int, input().split()))
        g = list(map(int, input().split()))
        b = list(map(int, input().split()))

        ob = Solution()
        print(ob.distinctColoring(N, r, g, b))
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/844b4fdcd988ac5461324d62d43f7892749a113c/1