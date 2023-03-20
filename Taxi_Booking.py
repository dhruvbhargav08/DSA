# This is from Geeks for Geeks.Question link at last
# You are going to book a taxi. 
# There are infinite number of points 1, 2, 3... on the X axis and your current position is cur. 
# There are N Taxis near you, and the position of those taxis is given as an array pos. 
# Where pos[i] denotes the position of the ith taxi. You are also given an array time. 
# Where time[i] denotes the time taken by the ith taxi to cover 1 unit of distance. 
# Your task is to find the minimum time to board a taxi.
from typing import List


class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        minn=99999999
        for i in range(N):
            temp=abs(pos[i]-cur)*time[i]
            if minn>temp:
                minn=temp
        return minn



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
        
        
        cur = int(input())
        
        
        pos=IntArray().Input(N)
        
        
        time=IntArray().Input(N)
        
        obj = Solution()
        res = obj.minimumTime(N, cur, pos, time)
        
        print(res)
        

# } Driver Code Ends
# Quesiton link 
# https://practice.geeksforgeeks.org/problems/7995e41d167d81f14f1d4194b29ef839f52d18ba/1