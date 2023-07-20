#This is from Geeks for Geeks.Question link at last
# Given a string S consisting of lowercase Latin Letters. 
# Return the first non-repeating character in S. 
# If there is no non-repeating character, return '$'.
#User function Template for python3

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        n=len(s)
        dictt={}
        for i in range (n):
            if s[i] not in dictt:
                dictt[s[i]]=1
            else:
                dictt[s[i]]+=1
        for i in s:
            if dictt[i]==1:
                return i
        return '$'
        
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        ans=obj.nonrepeatingCharacter(s)
        if(ans!='$'):
            print(ans)
        else:
            print(-1)
            
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/non-repeating-character-1587115620/1