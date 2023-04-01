#This is from Geeks for Geeks.Question link at last
# You are given an integer N. 
# Consider an array arr having N elements where arr[i] = 2*i+1. (The array is 0-indexed)
# You are allowed to perform the given operation on the array any number of times:
# 1) Select two indices i and j and increase arr[i] by 1 and decrease arr[j] by 1.
# Your task is to find the minimum number of such operations required to make all the elements of the array equal.
#User function Template for python3

class Solution:
    def minOperations(self, N):
        # Code here
        if N%2:
            return (N//2)*((N//2)+1)
        else:
            return (N//2)*(N//2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N =int(input())
        ob = Solution()
        print(ob.minOperations(N))
        
        T -= 1

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/1f05c7c12b1084f270c57566b2110967c046730d/1