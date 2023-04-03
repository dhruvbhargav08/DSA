#This is from Geeks for Geeks.Question link at last
# Given an array of n distinct elements. 
# Find the minimum number of swaps required to sort the array in strictly increasing order.


class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, arr):
		#Code here
            n=len(arr)
            listt=[[arr[i],i] for i in range (n)]
            listt.sort()
            res,i=0,0
            while i<n:
                j=listt[i][1]
                if j==i:
                    i+=1
                    continue
                listt[i],listt[j]=listt[j],listt[i]
                res+=1
            return res
#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/minimum-swaps/1?page=1&difficulty[]=1&status[]=unsolved&curated[]=1&sortBy=submissions