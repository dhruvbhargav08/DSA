#This is from Geeks for Geeks.Question link at last#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n,x):
        #Your code here
        for i in range (n-1):
            s=set()
            for j in range (i+1,n):
                temp=x-(arr[i]+arr[j])
                if temp in s:
                    return 1
                else:
                    s.add(arr[j])
        return 0

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
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions