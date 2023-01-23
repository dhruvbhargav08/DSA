#This is from Geeks for Geeks.Question link at last
# Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N.
# Find the minimum number of coins and/or notes needed to make the change for Rs N. You must return the list containing the value of coins required.
#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        listt=[]
        arr=[1,2,5,10,20,50,100,200,500,2000]
        i=9
        while i>=0:
            if arr[i]>N:
                i-=1
            else:
                while arr[i]<=N:
                    listt.append(arr[i])
                    N-=arr[i]
        return listt

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends 
# Question link
# https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions