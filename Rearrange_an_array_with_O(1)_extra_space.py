# This is from Geeks for Geeks.Question link at last
# Given an array arr[] of size N where every element is in the range from 0 to n-1. 
# Rearrange the given array so that the transformed array arrT[i] becomes arr[arr[i]].
# NOTE: arr and arrT are both same variables, representing the array before and after transformation respectively.
#User function Template for python3

##Complete this code

class Solution:
    #Function to rearrange an array so that arr[i] becomes arr[arr[i]]
    #with O(1) extra space.
    def arrange(self,arr, n): 
        #Your code here
        for i in range (n):
            arr[i]=(arr[arr[i]]%n)*n+arr[i]
        for i in range(n):
            arr[i]=arr[i]//n
        return arr

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
            ob.arrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/rearrange-an-array-with-o1-extra-space3142/1