# This is from Geeks for Geeks.Question link at last
# Given an array Arr[] of N positive integers. 
# The task is to find the maximum of j - i subjected to the constraint of Arr[i] <= Arr[j].
#User function Template for python3
class Solution:

	def maxIndexDiff(self,arr,n):
		#code here
            temp=0
            i=0
            while i<n:
                j=n-1
                maxx=0
                while i<j:
                    if arr[i]<=arr[j]:
                        maxx=j-i
                        break
                    j-=1
                if temp<maxx:
                    temp=maxx
                i+=1
            return temp

#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/maximum-index3307/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions