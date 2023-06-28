# This is from Geeks for Geeks.Question link at last.
# For a given non-negative integer N, find the next smallest Happy Number. 
# A number is called Happy if it leads to 1 after a sequence of steps. 
# Wherein at each step the number is replaced by the sum of squares of its digits that is, if we start with Happy Number and keep replacing it with sum of squares of its digits, we reach 1 at some point.
#User function Template for python3


class Solution:
    def nextHappy (self, N):
        # code here
        def helper(n):
            if n==1:
                return True 
            if n==4:
                return False 
            temp=0
            for i in str(n):
                temp+=int(i)**2
            return helper(temp)
        while True :
            N+=1
            if helper(N):
                return N
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/next-happy-number4538/1