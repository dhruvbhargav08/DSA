#This is from Geeks for Geeks.Question link at last
# You are given an array of integers of size n where n being even.. 
# You have to calculate the number of dominate pairs (i,j) . 
# Where a pair is called dominant if ( 0<=i<n/2, n/2<=j<n, arr[i]>=5*arr[j] ) these relation are fulfilled.  
# For example  in arr=[10,3,3,1] index i=0, j=3 form a dominating pair
# Note : 0 based indexing is used  and n is even 
from typing import List


class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        # code here
        count=0
        listt1,listt2=arr[0:n//2],arr[n//2:n] 
        listt1.sort()
        listt2.sort()
        i,j=n//2-1,n//2-1
        while i>-1 and j>-1:
            if listt1[i]>=5*listt2[j]:
                count=count+j+1
                i-=1
            else:
                j-=1
        return count




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
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.dominantPairs(n, arr)
        
        print(res)
        

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/2a1c11024ceae36363fc405e07f2fa3e2f896ef0/1