#This is from Geeks for Geeks.Question link at last
# Given an array Arr of N positive integers and an integer K, find K largest elements from the array.  
# The output elements should be printed in decreasing order.
#User function Template for python3
class Solution:

	def kLargest(self,arr, n, k):
		# code here
            listt=[0]*k
            arr.sort()
            arr.reverse()
            for i in range (k):
                listt[i]=arr[i]
            return listt

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/k-largest-elements4206/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions