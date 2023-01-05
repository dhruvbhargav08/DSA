#This is from Geeks for Geeks.Question link at last
# Given an array of integers. Find the Inversion Count in the array. 
# Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. 
# If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        return self.mergesort(arr,0,len(arr)-1)
    def mergesort(self,arr,left,right):
        inversecount=0
        if left<right:
            mid=int(left+(right-left)/2)
            inversecount+=self.mergesort(arr,left,mid)
            inversecount+=self.mergesort(arr,mid+1,right)
            inversecount+=self.merge(arr,left,mid,right)
        return inversecount
    def merge(self,arr,left,mid,right):
        i=left
        j=mid+1
        k=0
        temp=[0]*(right-left+1)
        count=0
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                temp[k]=arr[i]
                k+=1
                i+=1
            else:
                temp[k]=arr[j]
                count+=mid+1-i
                k+=1
                j+=1
        while i<=mid:
            temp[k]=arr[i]
            k+=1
            i+=1
        while j<=right:
            temp[k]=arr[j]
            k+=1
            j+=1
        k=0
        for i in range(left,right+1):
            arr[i]=temp[k]
            k+=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?page=1&difficulty[]=1&status[]=solved&curated[]=1&sortBy=submissions