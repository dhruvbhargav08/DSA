# This is from Geeks for Geeks.Question link at last
# You are given an array of N elements and num queries, In each query you are given three numbers L,R and K and you have to tell, how many indexes are there in between L and R(L<=i<=R) such that the frequency of a[i] from index i to n-1 is k.
# Note: 0-based indexing
from typing import List



class Solution:
    def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        # code here
        def helper(arr,i):
            return arr.count(i)
        res=[]
        listt=[]
        for i in range (N):
            listt.append([A[i],helper(A[i:],A[i]),i])
        for L,R,K in Q:
            flag=0
            for i in range (L,R+1):
                count=listt[i][1]
                if count==K:
                    flag+=1
            res.append(flag)
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



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        num = int(input())
        
        
        A=IntArray().Input(N)
        
        
        Q=IntMatrix().Input(num, 3)
        
        obj = Solution()
        res = obj.solveQueries(N, num, A, Q)
        
        IntArray().Print(res)
        

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/ad6699d4aaf84c74b119fac3b65e9ceb3fc8ef14/1