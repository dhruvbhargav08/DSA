#This is from Geeks for Geeks.Question link at last
# Given an unsorted array Arr of size N of positive integers. 
# One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. 
# Find these two numbers.
#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        arr.sort()
        summ=0
        count=1
        missing=0
        access=0
        actualsum=0
        for i in range(n):
            if arr[i]==arr[i-1]:
                access=arr[i]
            actualsum+=count
            summ+=arr[i]
            count+=1
        missing=actualsum-summ+access
        return [access,missing]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
# https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions