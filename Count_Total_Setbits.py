#This is from Geeks for Geeks.Question link at last.
# You are given a number N. 
# Find the total number of setbits in the numbers from 1 to N. 
class Solution:
    def countBits(self, n : int) -> int:
        # code here
        if n<=1:
            return n
        x=self.helper(n)
        return (x*(2**(x-1))+(n-(2**x)+1)+self.countBits(n-(2**x)))
    def helper(self,n):
        x=0
        while 2**x<=n:
            x+=1
        return x-1
#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        obj = Solution()
        res = obj.countBits(N)
        
        print(res)
        
# } Driver Code Ends
# https://practice.geeksforgeeks.org/problems/1132bd8ee92072cd31441858402641d6800fa6b3/1