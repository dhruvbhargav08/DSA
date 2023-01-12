#This is from Geeks for Geeks.Question link at last
# Given an array Arr[] that contains N integers (may be positive, negative or zero). 
# Find the product of the maximum product subarray.
#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
            maxx=-99999 
            curr=1
            lastt=1
            for i in range(len(arr)):
                curr*=arr[i]
                lastt*=arr[n-i-1]
                maxx=max(maxx,lastt,curr)
                if curr==0:
                    curr=1
                if lastt==0:
                    lastt=1
            return maxx

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions