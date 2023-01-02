#This is from Geeks for Geeks.Question link at last
# Given an array arr[] denoting heights of N towers and a positive integer K.
# For each tower, you must perform exactly one of the following operations exactly once.
# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.
# You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.
#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        anss=arr[n-1]-arr[0]
        maxx,minn=0,0
        for i in range(1,n):
            if arr[i]>=k:
                maxx=max(arr[i-1]+k,arr[n-1]-k)
                minn=min(arr[i]-k,arr[0]+k)
                anss=min(anss,maxx-minn)
        return anss

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
#Question link
# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions