#This is from Geeks for Geeks.Question link at last
# Given a boolean 2D array of n x m dimensions where each row is sorted. 
# Find the 0-based index of the first row that has the maximum number of 1's.
#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
            maxx=0
            index=0
            for i in range (n):
                curr=0
                for j in range (m):
                    if arr[i][j]==1:
                        curr+=1
                if curr>maxx:
                    maxx=curr
                    index=i
            if maxx==0:
                return -1
            return index

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions