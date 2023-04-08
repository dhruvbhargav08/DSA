#This is from Geeks for Geeks.Question link at last
# Given an array of positive and negative integers. 
# You have to make the array beautiful. 
# An array is beautiful if two adjacent integers, arr[i] and arr[i+1] have the same sign. 
# And you can do the following operation any number of times until the array becomes beautiful.
# If two adjacent integers have different signs, remove them.
# Return the beautiful array after performing the above operation.
# Note: An empty array is also a beautiful array. 
# There can be many adjacent integers with different signs. 
# So remove adjacent integers with different signs from left to right.
#User function Template for python3

from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        N=len(arr)
        i=1
        def sign(listt):
            count=0
            for j in listt:
                if j<0:
                    count-=1
                elif j>=0:
                    count+=1
            if count==0:
                return True
            else:
                return False
        stack=[]
        stack_len=0
        for i in range(N):
            if stack_len==0:
                stack.append(arr[i])
                stack_len+=1
            else:
                if sign([stack[-1],arr[i]]):
                    stack.pop()
                    stack_len-=1
                else:
                    stack.append(arr[i])
                    stack_len+=1
         
        return stack

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        arr = list(map(int,input().split()))
        
        obj = Solution()
        res = obj.makeBeautiful(arr)
        print(*res)
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/badefd58bace4f2ca25267ccfe0c9dc844415e90/1