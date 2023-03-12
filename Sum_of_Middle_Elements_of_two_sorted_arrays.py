# This is from Geeks for Geeks.Question link at last
# Given 2 sorted arrays Ar1 and Ar2 of size N each. 
# Merge the given arrays and find the sum of the two middle elements of the merged array.
#User function Template for python3

class Solution:
	def findMidSum(self, ar1, ar2, n): 
		# code here 
            num1,num2=0,0
            i,j,k=0,0,0
            while i<n and j<n:
                if ar1[i]<ar2[j]:
                    if k==n-1:
                        num1=ar1[i]
                    if k==n:
                        num2=ar1[i]
                    i+=1
                    k+=1
                else:
                    if k==n-1:
                        num1=ar2[j]
                    if k==n:
                        num2=ar2[j]
                    j+=1
                    k+=1
            while i<n:
                if k==n-1:
                    num1=ar1[i]
                if k==n:
                    num2=ar1[i]
                i+=1
                k+=1
            while j<n:
                if k==n-1:
                    num1=ar2[j]
                if k==n:
                    num2=ar2[j]
                j+=1
                k+=1
            summ=num1+num2
            return summ

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ar1=list(map(int, input().strip().split()))
        ar2=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc=tc-1

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays2305/1?page=1&difficulty[]=1&status[]=unsolved&curated[]=1&sortBy=submissions