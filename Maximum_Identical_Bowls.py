# This is from Geeks for Geeks.Question link at last
# There are N bowls containing cookies. 
# In one operation, you can take one cookie from any of the non-empty bowls and put it into another bowl. 
# If the bowl becomes empty you discard it. You can perform the above operation any number of times. 
# You want to know the maximum number of bowls you can have with an identical number of cookies.
# Note: All the non-discarded bowls should contain the identical number of cookies.

from typing import List
class Solution:
    def getMaximum(self, N : int, arr : List[int]) -> int:
        # code here
        summ=sum(arr)
        while True :
            if summ%N==0:
                return N
            N-=1
        return -1 



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
        
        N = int(input())
        
        
        arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.getMaximum(N, arr)
        
        print(res)
        

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/5bfe93cc7f5a214bc6342709c78bc3dceba0f1c1/1