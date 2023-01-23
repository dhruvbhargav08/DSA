#This is from Geeks for Geeks.Question link at last
# Quick Sort is a Divide and Conquer algorithm. 
# It picks an element as a pivot and partitions the given array around the picked pivot.
# Given an array arr[], its starting position is low (the index of the array) and its ending position is high(the index of the array).

Note: The low and high are inclusive.

Implement the partition() and quickSort() functions to sort the array.
#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low<high:
            pi=self.partition(arr,low,high)
            self.quickSort(arr,low,pi-1)
            self.quickSort(arr,pi+1,high)
    def partition(self,arr,low,high):
        # code here
        pivot=arr[high]
        i=low-1
        for j in range (low,high):
            if arr[j]<=pivot:
                i=i+1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/quick-sort/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions
