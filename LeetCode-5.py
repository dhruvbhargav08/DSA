# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"
 
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<=1:
            return s 
        maxString = s[0]
        maxLength = 1
        dp = [[False for j in range (n)] for i in range (n)]
        for i in range (n):
            dp[i][i] = True
            for j in range (i):
                if s[j]==s[i] and (i-j<=2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1>maxLength: 
                        maxLength = i-j+1
                        maxString = s[j:i+1]
        return maxString