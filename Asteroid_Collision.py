# This is from Geeks for Geeks.Question link at last
# We are given an integer array asteroids of size N representing asteroids in a row. 
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
# Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
# If both are of same size, both will explode. 
# Two asteroids moving in the same direction will never meet.


#User function Template for python3

class Solution:
    def asteroidCollision(self, N, arr):
        # Code here
        stack=[]
        for i in range (N):
            add=True
            while stack and (stack[-1]>0 and arr[i]<0):
                if abs(stack[-1])>abs(arr[i]):
                    add=False
                    break
                elif abs(stack[-1])==abs(arr[i]):
                    add=False
                    stack.pop()
                    break 
                else:
                    stack.pop()
            if add:
                stack.append(arr[i])
        return stack 
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/asteroid-collision/1