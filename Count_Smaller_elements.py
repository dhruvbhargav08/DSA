# This is from Geeks for Geeks.Question link at last
# Given an array Arr of size N containing positive integers. 
# Count number of smaller elements on right side of each array element.
#User function Template for python3
import bisect
class Solution:

	def constructLowerArray(self,arr, n):
            ans ,temp=[],[]
            for i in range (n-1,-1,-1):
                c=bisect.bisect_left(temp,arr[i])
                ans.append(c)
                temp.insert(c,arr[i])
            return ans[::-1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/count-smaller-elements2214/0