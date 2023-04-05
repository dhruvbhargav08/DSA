#This is from Geeks for Geeks.Question link at last
# Given an array A of n positive numbers. 
# The task is to find the first index in the array such that the sum of elements before it is equal to the sum of elements after it.
# Note:  Array is 1-based indexed.
# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equalSum(self,A, N):
        # Your code here
        left,right=0,sum(A)
        for i in range (N):
            if left+A[i]==right:
                return i+1
            right-=A[i]
            left+=A[i]
        return -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equalSum(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/78a6854c8a2915e05f236aa407dfaa1bbc8ae7d3/1