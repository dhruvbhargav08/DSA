#This is from Geeks for Geeks.Question link at last
# Given an unsorted array, Arr[] of size N and that contains even number of occurrences for all numbers except two numbers. 
# Find the two numbers in decreasing order which has odd occurrences.
#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        a=set()
        for i in range (N):
            if Arr[i] in a:
                a.remove(Arr[i])
            else:
                a.add(Arr[i])
        listt=list(a)
        listt.sort()
        return listt[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions