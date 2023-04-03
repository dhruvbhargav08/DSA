#This is from Geeks for Geeks.Question link at last
# Given a matrix of size n x m, where every row and column is sorted in increasing order, and a number x. 
# Find whether element x is present in the matrix or not.

#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def search(self,matrix, n, m, x): 
    	# code here 
            r,c=0,m-1
            while r<n and c>-1:
                if matrix[r][c]==x:
                    return True
                elif matrix[r][c]>x:
                    c-=1
                else:
                    r+=1
            return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		size = input().strip().split()
		r = int(size[0])
		c = int(size[1])
		line = input().strip().split()
		matrix = [ [0 for _ in range(c)] for _ in range(r) ]
		for i in range(r):
			for j in range(c):
				matrix[i][j] = int( line[i*c+j] )
		target = int(input())
		obj = Solution()
		if (obj.search(matrix,r,c,target)): 
			print(1) 
		else: 
			print(0) 


# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1?page=1&difficulty[]=1&status[]=unsolved&curated[]=1&sortBy=submissions