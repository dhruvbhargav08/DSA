#This is from Geeks for Geeks.Question link at last
# Given a string str, find the minimum characters to be added at front of the string to make it a palindrome./
#User function Template for python3

class Solution:
    def addMinChar (self, str1):
        # code here 
        def ispal(strr,n):
            i,j=0,n-1
            while i<j:
                if strr[i]!=strr[j]:
                    return False
                i+=1
                j-=1
            return True
        N=len(str1)
        count=0
        for i in range (N-1,-1,-1):
            if ispal(str1[0:i+1],i+1):
                return N-i-1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str1 = input()

        ob = Solution()
        print(ob.addMinChar(str1))

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/55dbfdc246f3f62d6a7bcee7664cacf6be345527/1