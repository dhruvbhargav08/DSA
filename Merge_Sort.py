#This is from Geeks for Geeks.Question link at last
# Given an array arr[], its starting position l and its ending position r. 
# Sort the array using merge sort algorithm
#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        n1=m-l+1
        n2=r-m
        l1=arr[l:l+n1]
        
        l2=arr[m+1:m+1+n2]
        i=0
        j=0
        k=l
        while i<n1 and j<n2:
            if l1[i]<=l2[j]:
                arr[k]=l1[i]
                i+=1
            else:
                arr[k]=l2[j]
                j+=1
            k+=1
        while i<n1:
            arr[k]=l1[i]
            i+=1
            k+=1
        while j<n2:
            arr[k]=l2[j]
            j+=1
            k+=1
    def mergeSort(self,arr, l, r):
        #code here
        if (l < r) :
            m = (l+r)//2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/merge-sort/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions