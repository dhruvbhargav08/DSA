# This is from Geeks for Geeks.Question link at last
# Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. 
# It is given that all array elements are distinct.
# Note :-  l and r denotes the starting and ending index of the array.
#User function Template for python3

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        ''' 
        def helper1(arr,l,r):
            pivot=arr[r]
            pivotloc=l
            for i in range (l,r+1):
                if arr[i]<pivot:
                    arr[i],arr[pivotloc]=arr[pivotloc],arr[i]
                    pivotloc+=1
            arr[r],arr[pivotloc]=arr[pivotloc],arr[r]
            return pivotloc
        def helper2(arr,l,r,k):
            temp=helper1(arr,l,r)
            if temp==k:
                return arr[k]
            elif temp<k:
                return helper2(arr,temp+1,r,k)
            else:
                return helper2(arr,l,temp-1,k)
        return helper2(arr,l,r,k-1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1