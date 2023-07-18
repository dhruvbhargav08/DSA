#This is from Geeks for Geeks.Question link at last
# Given an array of n positive integers. 
# Find the sum of the maximum sum subsequence of the given array such that the integers in the subsequence are sorted in strictly increasing order i.e. a strictly increasing subsequence. 
#User function Template for python3
class Solution:
	def maxSumIS(self, arr, n):
		# code here
            msis=[x for x in arr]
            for i in range(1, len(arr)):
                for j in range(i):
                    if(arr[j]<arr[i]):
                        msis[i]=max(msis[i], arr[i]+msis[j])
            return max(msis)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1?page=1&difficulty[]=1&status[]=unsolved&category[]=Dynamic%20Programming&sortBy=submissions