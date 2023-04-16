#This is from Geeks for Geeks.Question link at last
# You are given two arrays A and B each of length N. 
# You can perform the following operation on array A zero or more times. 
# Select any two indices i and j, 1 <= i , j <= N and i != j
# Set A[i] = A[i] + 2 and A[j] = A[j]-2
# Find the minimum number of operations required to make A and B equal.
# Note :
# Two arrays are said to be equal if the frequency of each element is equal in both of them.
# Arrays may contain duplicate elements.
from typing import List
class Solution:
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        count=0
        A.sort()
        B.sort()
        if sum(A)!=sum(B):
            return -1
        Aevenodd,Bevenodd=[[],[]],[[],[]]
        for i in range (N):
            Aevenodd[A[i]%2].append(A[i])
            Bevenodd[B[i]%2].append(B[i])
        countaeven,countaodd,countbeven,countbodd=len(Aevenodd[0]),len(Aevenodd[1]),len(Bevenodd[0]),len(Bevenodd[1])
        if countaeven!=countbeven and countaodd!=countbodd:
            return -1
        for i in range (countaeven):
            count=count+(abs(Aevenodd[0][i]-Bevenodd[0][i]))//2
        for i in range (countbodd):
            count=count+(abs(Aevenodd[1][i]-Bevenodd[1][i]))//2
        return count//2


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
        
        
        A=IntArray().Input(N)
        
        
        B=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, A, B)
        
        print(res)
        

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/4db2fcd97400456c4914d5a3e8ad932cc21e3e9d/1