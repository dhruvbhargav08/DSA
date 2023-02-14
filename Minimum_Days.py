# This is from Geeks for Geeks.Question link at last
# Given a string S of length N containing only lowercase alphabets. 
# You are also given a permutation P of length N containing integers from 0 to N-1. 
# In (i+1)'th day you can take the P[i] value of the permutation array and replace S[P[i]] with a '?'.
# For example in day 1, we can choose index of permutation array is i=0 and replace S[P[0]] with '?'.
# Similarly in day 2, we can choose index of permutation array is i=1. You can replace S[P[1]] with '?'.
# Similarly in day 3,we can choose index of permutation array is i=2. You can replace S[P[2]] with '?'.
# You have to tell the minimum number of days required, such that after it for all index i (0<=i<N-1), if S[i]!='?', then S[i]!=S[i+1].
from typing import List


class Solution:
    def getMinimumDays(self, N : int, S : str, P : List[int]) -> int:
        # code here
        count= 0
        S = list(S)
        for i in range(N - 1):
            if(S[i]==S[i+1]) : count+=1
        if count==0 : 
            return 0
        for i in range(N):
            temp=P[i]
            if temp-1>=0 and S[temp-1]==S[temp]: 
                count-=1
            if temp+1<N and S[temp]==S[temp+1]:
                count-=1
            S[temp]='?'
            if(count==0):
                return i+1




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
        
        
        S = (input())
        
        
        P=IntArray().Input(N)
        
        obj = Solution()
        res = obj.getMinimumDays(N, S, P)
        
        print(res)
        

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/f4d22b1f9d62e8bee0ff84e9fa51dc66eb5005ec/0