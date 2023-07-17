# #This is from Geeks for Geeks.Question link at last
# Given two strings s and t. Return the minimum number of operations required to convert s to t.
# The possible operations are permitted:
# Insert a character at any position of the string.
# Remove any character from the string.
# Replace any character from the string with any other character.
class Solution:
	def editDistance(self, s, t):
		# Code here
            m,n=len(s),len(t)
            dp=[[0 for j in range (n+1)] for i in range (m+1)]
            for i in range (m+1):
                for j in range (n+1):
                    if i==0:
                        dp[i][j]=j
                    elif j==0:
                        dp[i][j]=i
                    elif s[i-1]==t[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
            return dp[m][n]


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends
# Quetion link 
# https://practice.geeksforgeeks.org/problems/edit-distance3702/1?page=1&difficulty[]=1&status[]=unsolved&category[]=Dynamic%20Programming&sortBy=submissions