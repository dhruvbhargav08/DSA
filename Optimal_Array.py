# This is from Geeks for Geeks.Question link at last
# You are given a sorted array a of length n. 
# For each i(0<=i<=n-1), you have to make all the elements of the array from index 0 till i equal, using minimum number of operations. 
# In one operation you either increase or decrease the array element by 1.
# You have to return a list which contains the minimum number of operations for each i, to accomplish the above task.
# Note:
# 1. 0-based indexing.
# 2. For each index, you need to consider the same array which was given to you at the start.
from typing import List


class Solution:
    def optimalArray(self, n : int, a : List[int]) -> List[int]:
        # code here
        res=[0]
        for i in range (1,n):
            res.append(res[0]+res[i-1]+abs(a[i]-a[i//2]))
        return res



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        a=IntArray().Input(n)
        
        obj = Solution()
        res = obj.optimalArray(n, a)
        
        IntArray().Print(res)
        

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/d4aeef538e6dd3280dda5f8ed7964727fdc7075f/1