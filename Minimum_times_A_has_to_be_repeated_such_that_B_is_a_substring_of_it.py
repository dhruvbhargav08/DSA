#This is from Geeks for Geeks.Question link at last
# Given two strings A and B. Find minimum number of times A has to be repeated such that B is a Substring of it. 
# If B can never be a substring then return -1.
#User function Template for python3

class Solution:
    def minRepeats(self, a, b):
        # code here 
        lena,lenb=len(a),len(b)
        count=1
        i,j=0,0
        while i<lena:
            if b[0]==a[i]:
                break
            i+=1
        if i==lena:
            return -1
        while j<lenb:
            if i==lena:
                i=0
                count+=1
            if a[i]!=b[j]:
                return -1
            if a[i]==b[j]:
                j+=1
                i+=1
            
            
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/fda70097eb2895ecfff269849b6a8aace441947c/1