# This is from Geeks for Geeks.Question link at last
# Given a dictionary of words where each word follows CamelCase notation, print all words (in lexicographical order) in the dictionary that match with a given pattern consisting of uppercase characters only.
# Example: GeeksForGeeks matches the pattern "GFG", because if we combine all the capital letters in GeeksForGeeks they become GFG.
# CamelCase is the practice of writing compound words or phrases such that each word or abbreviation begins with a capital letter. 
# Common examples include PowerPoint and Wikipedia, GeeksForGeeks, CodeBlocks, etc.
#User function Template for python3

class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        #code here
        listt=[]
        ans=[]
        for i in range (N):
            strr=""
            for j in Dictionary[i]:
                if 65<=ord(j)<=90:
                    strr+=j
            listt.append([strr,i])
        lenn=len(Pattern)
        for i,j in listt:
            k=0
            for m in i :
                if m!=Pattern[k]:
                    break
                if m==Pattern[k]:
                    k+=1
                if k==lenn:
                    ans.append(Dictionary[j])
                    break
        if len(ans)==0:
            return [-1]
        return ans 
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/camelcase-pattern-matching2259/1
