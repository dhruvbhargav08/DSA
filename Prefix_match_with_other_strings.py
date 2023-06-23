# This is from Geeks for Geeks.Question link at last
# Given an array of strings arr[] of size n, a string str and an integer k. 
# The task is to find the count of strings in arr[] whose prefix of length k matches with the k-length prefix of str.
#User function Template for python3

class Solution:
    def klengthpref(self,arr,n,k,s):
        # return list of words(str) found in the board
        count=0
        for i in range (n):
            flag=0
            for j in range (min(k,len(s),len(arr[i]))):
                if arr[i][j]==s[j]:
                    flag+=1
            if flag==k:
                count+=1
        return count
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr = []
        for x in range(n):
            s1 = input()
            arr.append(s1)
        k = int(input())
        s = input()
        obj = Solution()
        print(obj.klengthpref(arr,n,k,s))
        
        
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/prefix-match-with-other-strings/1