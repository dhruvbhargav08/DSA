#This is from Geeks for Geeks.Question link at last
# Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element key. 
# The task is to find the index of the given element key in the array A.
# The whole array A is given as the range to search.
#User function Template for python3

class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        # l: The starting index
        # h: The ending index, you have to search the key in this range
        # Complete this function
        res=-1
        N=len(A)
        def pivot(arr,N):
            start,end=0,N-1
            while start<end:
                mid=start+(end-start)//2
                if arr[0]<=arr[mid]:
                    start=mid+1
                else:
                    end=mid
            return start
        pivot=pivot(A,N)
        def binary(arr,k,N):
            start,end=0,N-1
            while start<=end:
                mid=start+(end-start)//2
                if arr[mid]==k:
                    return mid
                elif arr[mid]<k:
                    start=mid+1
                else:
                    end=mid-1
            return -1
        if A[0]<=key<=A[pivot-1]:
            res=binary(A[0:pivot],key,pivot)
        if A[pivot]<=key<=A[N-1]:
            res=binary(A[pivot:N],key,N-pivot)
            if res!=-1:
                res+=pivot
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1