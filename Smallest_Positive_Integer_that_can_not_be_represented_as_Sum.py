# This is from Geeks for Geeks.Question link at last
# Given an array of size N, 
# find the smallest positive integer value that is either not presented in the array or cannot be represented as a sum(coz sum means you are adding two or more elements) of some elements from the array.
#User function Template for python3

class Solution:
    def smallestpositive(self, array, n): 
        # Your code goes here  
        array.sort()
        ans=1
        for i in range(n):
          if ans<array[i]:
              return ans
          else:
              ans = ans+array[i]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.smallestpositive(array,n))


# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/b6b608d4eb1c45f2b5cace77c4914f302ff0f80d/0