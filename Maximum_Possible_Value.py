# This is from Geeks for Geeks.Question link at last
# Given two arrays A[] and B[] of same length N. 
# There are N types of sticks of lengths specified. 
# Each stick of length A[i] is present in B[i] units (i=1 to N). 
# You have to construct the squares and rectangles using these sticks. 
# Each unit of a stick can be used as length or breadth of a rectangle or as a side of square. 
# A single unit of a stick can be used only once.
# Let S be the sum of lengths of all sticks that are used in constructing squares and rectangles. 
# The task is to calulate the maximum possible value of S.
# Note: The element in array A[] is always unique.
#User function Template for python3
class Solution:
    def maxPossibleValue(self, N, A, B): 
        #code here
        count=0
        mini=99999999
        summ=0
        for i in range(N):
            n=B[i]//2
            if n>0:
                mini=min(mini,A[i])
                summ+=A[i]*n*2
                count+=n
        if count%2!=0:
            summ-=mini*2
        return summ

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPossibleValue(N, A, B)
        print(ans)

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/2d3fc3651507fc0c6bd1fa43861e0d1c43d4b8a1/1