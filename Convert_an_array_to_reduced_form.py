#This is from Geeks for Geeks.Question link at last
# Given an array with N distinct elements, convert the given array to a reduced form where all elements are in range from 0 to N-1. 
# The order of elements is same, i.e., 0 is placed in place of smallest element, 1 is placed for second smallest element, and N-1 is placed for the largest element.
# Note: You don't have to return anything. You just have to change the given array.
#User function Template for python3
class Solution:

	def convert(self,arr, n):
		# code here
            temp = [(arr[i], i) for i in range(0,n)]
            temp.sort()
            for i in range(0, n):
                arr[temp[i][1]] = i
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/convert-an-array-to-reduced-form1101/0