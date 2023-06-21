# This is from Geeks for Geeks.Question link at last
# You will be given an integer n, your task is to return the sum of all natural number less than or equal to n.
# As the answer could be very large, return answer modulo 109+7.
#User function Template for python3

class Solution:
    def sumOfNaturals(self, n):
        # code here 
        modd=1000000007
        summ=(n)*(n+1)//2
        summ=summ%modd
        return summ

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.sumOfNaturals(n))
# } Driver Code Ends
# Quetion link 
# https://practice.geeksforgeeks.org/problems/reverse-coding2452/1