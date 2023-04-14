#This is from Geeks for Geeks.Question link at last
# magine an imaginary array of length N containing balls. 
# Given 2 arrays color and radius of length N each, where color[i] represents the color of the ith ball while radius[i] represents the radius of ith ball. 
# If two consecutive balls have the same color and size, both are removed from the array. 
# Geek wants to know the length of the final imaginary array.
from typing import List


class Solution:
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        # code here
        stack=[]
        for i in range (N):
            if len(stack)==0:
                stack.append(i)
            else:
                if color[stack[-1]]==color[i] and radius[stack[-1]]==radius[i]:
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)


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
        
        
        color=IntArray().Input(N)
        
        
        radius=IntArray().Input(N)
        
        obj = Solution()
        res = obj.finLength(N, color, radius)
        
        print(res)
        

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/546ea68f97be7283a04ddcc8057e09b46a686471/1