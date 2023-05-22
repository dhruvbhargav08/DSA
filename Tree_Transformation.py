# This is from Geeks for Geeks.Question link at last
# You are given a tree containing N nodes in the form of an array P where Pi represents the parent of the i-th node and P0 = -1 as the tree is rooted at node 0. 
# In one move, you can merge any two adjacent nodes. 
# Calculate the minimum number of moves required to turn the tree into a star tree.
# -> Merging adjacent nodes means deleting the edge between them and considering both the nodes as a single one.
# -> A Star tree is a tree with a center node, and all other nodes are connected to the center node only.


from typing import List


class Solution:
    def solve(self, N : int, arr : List[int]) -> int:
        # code here
        count=0
        listt=[0]*N
        for i in range (1,N):
            listt[i]+=1
            listt[arr[i]]+=1
        for i in range(N):
            if listt[i]==1:
                count+=1
        return N-count-1
                



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
        
        
        p=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, p)
        
        print(res)
        

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/fbcd1787378ed396a8f24b47872cbc0ad2624f1d/1