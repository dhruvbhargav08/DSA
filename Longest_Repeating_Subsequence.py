#This is from Geeks for Geeks.Question link at last
# Given string str, find the length of the longest repeating subsequence such that it can be found twice in the given string.
# The two identified subsequences A and B can use the same ith character from string str if and only if that ith character has different indices in A and B. 
# For example, A = "xax" and B = "xax" then the index of first "x" must be different in the original string for A and B.
#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, strr):
		# Code here
            n=len(strr)
            dp=[[0 for j in range (n+1)]for i in range (n+1)]
            for i in range (n-1,-1,-1):
                for j in range (n-1,-1,-1):
                    if strr[i]==strr[j] and i!=j:
                        dp[i][j]=1+dp[i+1][j+1]
                    else:
                        dp[i][j]=max(dp[i+1][j],dp[i][j+1])
            return dp[0][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1
