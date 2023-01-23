# This is from Geeks for Geeks.Question link at last
# You are given an array, arr of length N, and also a single integer K . 
# Your task is to split the array arr into K non-overlapping, non-empty subarrays. 
# For each of the subarrays, you calculate the sum of the elements in it. 
# Let us denote these sums as S1, S2, S3, ..., SK. Where Si denotes the sum of the elements in the ith subarray from left.
# Let G = GCD( S1, S2 ,S3 , ..., SK).
# Find the maximum value of G that can be obtained. 
# The array may contain duplicate elements.


from typing import List
class Solution:
    def solve(self, N : int, K : int, arr : List[int]) -> int:
        # code here
        summ=sum(arr)
        factors=[]
        root=int(summ**0.5)
        for i in range (1,root+1):
            if summ%i==0:
                factors.append(i)
                if i!=(summ//i):
                    factors.append(summ//i)
        factors.sort(reverse=True)
        ans=1
        for i in range (1,N):
            arr[i]+=arr[i-1]
        n=len(factors)
        for i in factors:
            count=0
            for j in arr:
                if j%i==0:
                    count+=1
            if count>=K:
                ans=i
                break
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
        
        
        K = int(input())
        
        
        arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, K, arr)
        
        print(res)
        

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/2b70d42632a4e207569c6d2d777383e4603d6fe1/1?page=3&difficulty[]=1&status[]=solved&sortBy=submissions