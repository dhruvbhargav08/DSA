# This is from Geeks for Geeks.Question link at last
# There is a rectangular path for a Train to travel consisting of n rows and m columns. 
# The train will start from one of the grid's cells and it will be given a command in the form of string s consisting of characters L, R, D, U. 
# Find if it is possible to travel the train inside the grid only.
# Note:
# If the train is at position (i,j)
# on taking 'L' it goes to (i,j-1),
# on taking 'R' it goes to (i,j+1),
# on taking 'D' it goes to (i-1,j),
# on taking 'U' it goes to (i+1,j).#User function Template for python3

class Solution:
    def isPossible(self, n, m, s):
        # code here
        horizontal,vertical=0,0
        left,right,up,down=0,0,0,0
        for _ in s:
            if _=="L":
                horizontal+=1
            if _=="R":
                horizontal-=1
            if _=="D":
                vertical-=1
            if _=="U":
                vertical+=1
            if horizontal>=0:
                left=max(left,horizontal)
            else:
                right=min(right,horizontal)
            if vertical>=0:
                up=max(up,vertical)
            else:
                down=min(down,vertical)
        if left-right<m and up-down<n:
            return 1
        return 0
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        s = input()
        
        ob = Solution()
        print(ob.isPossible(n, m, s))
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/trace-path3840/1