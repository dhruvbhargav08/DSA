#This is from Geeks for Geeks.Question link at last
# Given an array A of positive integers. 
# Your task is to find the leaders in the array. 
# An element of array is leader if it is greater than or equal to all the elements to its right side. 
# The rightmost element is always a leader. 

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        listt=[]
        maxx=N-1
        for i in range (N-1,-1,-1):
            if A[i]>=A[maxx]:
                maxx=i
                listt.append(A[i])
        return listt[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?page=1&sortBy=submissions