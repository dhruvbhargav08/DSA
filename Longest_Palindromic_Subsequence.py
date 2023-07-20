#This is from Geeks for Geeks.Question link at last
# Given a String, find the longest palindromic subsequence.
# NOTE: Subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.
#User function Template for python3

class Solution:

    def longestPalinSubseq(self, S):
        # code here
        n=len(S)
        dp=[[0 for i in range (n)] for i in range (n)]
        for i in range (n):
            dp[i][i]=1
        for i in range (n-1,-1,-1):
            for j in range (i+1,n):
                if S[i]==S[j]:
                    if i==j-1:
                        dp[i][j]=2
                    else:
                        dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/longest-palindromic-subsequence-1612327878/1