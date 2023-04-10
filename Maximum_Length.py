#This is from Geeks for Geeks.Question link at last
# Given the maximum occurrences of a, b, and c in a string. 
# Your task is to make the largest length string containing only a, b, and c such that no three consecutive characters are the same. 
# Return the longest possible string length.

#User function Template for python3

class Solution():
    def solve(self, a, b, c):
        #your code goes here
        listt=[a,b,c]
        listt.sort()
        temp=(listt[0]+listt[1]+1)*2
        if max(a,b,c)>temp:
            return -1
        else:
            return sum(listt)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import Counter
for _ in range(int(input())):
    a, b, c=map(int,input().split())
    obj = Solution()
    res = obj.solve(a, b, c)
    
    print(res)
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/84963d7b5b84aa24f7807d86e672d0f97f41a4b5/1