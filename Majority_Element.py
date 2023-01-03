#This is from Geeks for Geeks.Question link at last
# Given an array A of N elements. Find the majority element in the array. 
# A majority element in an array A of size N is an element that appears more than N/2 times in the array.
#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        m=[0]*(1000001)
        for i in A:
            m[i]+=1
        for i in A:
            if m[i]>int(N/2):
                return i
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
#Question link
# https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions