#This is from Geeks for Geeks.Question link at last
# Given an array Arr[] of N integers. 
# Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        curr_sum=0
        max_sum=arr[0]
        if max(arr)<0:
            return max(arr)
        for i in range (N):
            curr_sum=curr_sum+arr[i]
            if(curr_sum>max_sum):
                max_sum=curr_sum
            if curr_sum<0:
                curr_sum=0
        return max_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
#Question link
# https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions