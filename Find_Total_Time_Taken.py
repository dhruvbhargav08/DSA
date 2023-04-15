#This is from Geeks for Geeks.Question link at last
# You are given an array arr of size n, containing the values in between 1 to n & time of size n, containing time in sec, you are asked to determine the total time taken in order to pick all the array elements from left to right but there is a condition, 
# If from left, previous elements are different it takes 1 Sec to pick & if element got repeated then it will take time[arr[i]].
from typing import List


class Solution:
    def totalTime(self, n : int, arr : List[int], time : List[int]) -> int:
        # code here
        count=-1
        dictt = {}
        for i in range(n):
            if arr[i] in dictt:
                dictt[arr[i]]+=1
                count+=time[arr[i]-1]
            else:
                dictt[arr[i]] = 1
                count+=1
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
        
        
        time=IntArray().Input(n)
        
        obj = Solution()
        res = obj.totalTime(n, arr, time)
        
        print(res)
        

# } Driver Code Ends
# uestion link 
# https://practice.geeksforgeeks.org/problems/5ae4f296db3e6bb74641c4087d587b6f89d9d135/1