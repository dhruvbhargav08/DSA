#This is from Geeks for Geeks.Question link at last
# Given an array of N integers arr[] where each element represents the max length of the jump that can be made forward from that element. 
# Find the minimum number of jumps to reach the end of the array (starting from the first element). 
# If an element is 0, then you cannot move through that element.
# Note: Return -1 if you can't reach the end of the array.
#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
	    #code here
        nums = arr
        onplace=0
        jumps=0
        distance=0
        for i in range(len(nums)-1):
            distance = max(distance,i+nums[i])
            if i==onplace:
                onplace=distance
                jumps+=1
            if i>=distance:
                return -1
        return jumps

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends
#Question link
# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1?page=1&difficulty[]=1&sortBy=submissions