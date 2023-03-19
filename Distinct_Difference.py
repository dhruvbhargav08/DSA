# This is from Geeks for Geeks.Question link at last
# Given an array A[] of length N. 
# For each index i (1<=i<=N), find the diffference between the number of distinct element in it's left and right side in the array.
from typing import List


class Solution:
    def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
        # code here
        set_left=set()
        set_right=set()
        left=[0]*N
        right=[0]*N
        res=[0]*N
        len_left=0
        len_right=0
        for i in range (N):
            left[i]=len_left
            if A[i] not in set_left:
                len_left+=1
                set_left.add(A[i])
        for i in range (N-1,-1,-1):
            right[i]=len_right
            if A[i] not in set_right:
                len_right+=1
                set_right.add(A[i])
        for i in range (N):
            res[i]=left[i]-right[i]
        return res
        


#{ 
 # Driver Code Starts
# class IntArray:

#     def __init__(self) -> None:
#         pass
    
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        A=[int(i) for i in input().split()]
        
        obj = Solution()
        res = obj.getDistinctDifference(N, A)
        
        print(*res)
        

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/c670bf260ea9dce6c5910dedc165aa403f6e951d/1 