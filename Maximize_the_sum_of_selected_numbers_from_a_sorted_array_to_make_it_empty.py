#This is from Geeks for Geeks.Question link at last
# Given a array of N numbers, we need to maximize the sum of selected numbers. 
# At each step, you need to select a number Ai, delete one occurrence of Ai-1 (if exists), and Ai each from the array. 
# Repeat these steps until the array gets empty. The problem is to maximize the sum of the selected numbers.
# Note: Numbers need to be selected from maximum to minimum.
#User function Template for python3

class Solution:
    
    def maximizeSum (self,arr, n) : 
        #Complete the function
        m=[0]*(100001)
        summ=0
        for x in arr:
            m[x]+=1
        for i in range (n-1,-1,-1):
            curr=arr[i]
            if m[curr]!=0:
                summ+=curr
                m[curr]-=1
                if m[curr-1]!=0:
                    m[curr-1]-=1
        return summ


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    ob=Solution()
    
    ans = ob.maximizeSum(arr, n)
    print(ans)
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/maximize-the-sum-of-selected-numbers-from-an-array-to-make-it-empty0836/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions