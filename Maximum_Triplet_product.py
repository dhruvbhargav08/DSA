# This is from Geeks for Geeks.Question link at last
# Given an array arr of size n, the task is to find the maximum triplet product in the array.
#User function Template for python3

class Solution:
    def maxTripletProduct (self, arr,  n): 
        #Complete the function
        arr.sort()
        maxx1=arr[n-1]*arr[n-2]*arr[n-3]
        maxx2=arr[0]*arr[1]*arr[n-1]
        return max(maxx1,maxx2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.maxTripletProduct(arr, n)
    print(res)
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/d54c71dc974b7db3a200eb63f34e3d1cba955d86/1
