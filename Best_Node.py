# This is from Geeks for Geeks.Question link at last
# You are given a tree rooted at node 1. 
# The tree is given in form of an array P where Pi denotes the parent of node i, Also P1 = -1, as 1 is the root node. 
# Every node i has a value Ai associated with it. At first, you have to choose any node to start with, after that from a node you can go to any of its child nodes. 
# You've to keep moving to a child node until you reach a leaf node. 
# Every time you get to a new node, you write its value. 
# Let us assume that the integer sequence in your path is B.
# Let us define a function f over B, which is defined as follows:
# f(B) = B1 - B2 + B3 - B4 + B5.... + (-1)(k-1)Bk.
# You have to find the maximum possible value of f(B).
from typing import List


class Solution:
    def bestNode(self, N : int, A : List[int], P : List[int]) -> int:
        # code here
        non_leaf=set(P)
        leaf=[]
        for i in range (N):
            if i not in non_leaf:
                leaf.append(i)
        ans=-999999999
        for i in leaf:
            node=i
            flag=0
            while node!=-1:
                flag*=-1
                flag+=A[node-1]
                node=P[node-1]
                ans=max(ans,flag)
        return ans 



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
        
        
        P=IntArray().Input(N)
        
        obj = Solution()
        res = obj.bestNode(N, A, P)
        
        print(res)
        

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/a3493283697b7b69573a840f371a55ccd9332bb0/1