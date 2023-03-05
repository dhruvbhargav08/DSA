# This is from Geeks for Geeks.Question link at last
# A special compression mechanism can arbitrarily delete 0 or more characters and replace them with the deleted character count.
# Given two strings, S and T where S is a normal string and T is a compressed string, determine if the compressed string  T is valid for the plaintext string S. 
#User function Template for python3

class Solution:
    def checkCompressed(self, s, t):
        # code here 
        i,j=0,0
        lens,lent=len(s),len(t)
        while i<lens and j<lent:
            if s[i]==t[j]:
                i+=1
                j+=1
            elif 48<=ord(t[j])<=57:
                num=0
                while j<lent and (48<=ord(t[j])<=57):
                    num*=10
                    num+=int(t[j])
                    j+=1
                i+=num
            else:
                return 0
        if i==lens and j==lent:
            return 1
        else:
            return 0
        
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        T = input()
        
        ob = Solution()
        print(ob.checkCompressed(S,T))
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/13eb74f1c80bc67d526a69b8276f6cad1b8c3401/1