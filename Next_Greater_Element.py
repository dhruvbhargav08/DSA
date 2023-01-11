#This is from Geeks for Geeks.Question link at last
# Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
# Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
# If there does not exist next greater of current element, then next greater element for current element is -1. 
# For example, next greater of the last element is always -1.
#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        temp=[]
        listt=[]
        for i in range(n-1,-1,-1):
            while(len(listt)!=0 and a[i]>=listt[-1]):
                listt.pop()
            if(len(listt)!=0):
                temp.append(listt[-1])
            else:
                temp.append(-1)
            listt.append(arr[i])
        return temp[::-1] 

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

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions