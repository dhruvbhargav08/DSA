#This is from Geeks for Geeks.Question link at last
# Given a sorted array of positive integers. 
# Your task is to rearrange the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.
# Note: Modify the original array itself. Do it without using any extra space. 
# You do not have to return anything.
#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        high=n-1
        low=0
        listt=[0]*n
        index=0
        while high>=low:
            try:
                listt[index]=arr[high]
                index+=1
                high-=1
                listt[index]=arr[low]
                index+=1
                low+=1
            except:
                pass
        for i in range (n):
            arr[i]=listt[i]
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
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions