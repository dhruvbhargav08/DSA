#This is from Geeks for Geeks.Question link at last.
# Given an array arr[] of size N and an integer K. 
# Find the maximum for each and every contiguous subarray of size K.
#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        #User function Template for python3
        #code here
        temp=deque()
        res=[]
        for i in range(n):
            if len(temp)>0 and temp[0]==i-k:
                temp.popleft()
            while len(temp)>0 and arr[i]>=arr[temp[-1]]:
                temp.pop()
            temp.append(i)
            if i>=k-1:
                res.append(arr[temp[0]])
        return res
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions
