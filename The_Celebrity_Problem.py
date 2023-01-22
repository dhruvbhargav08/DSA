#This is from Geeks for Geeks.Question link at last
# A celebrity is a person who is known to all but does not know anyone at a party. 
# If you go to a party of N people, find if there is a celebrity in the party or not.
# A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j  is set to 1 it means ith person knows jth person. 
# Here M[i][i] will always be 0.
# Note: Follow 0 based indexing.
# Follow Up: Can you optimize it to O(N)
#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        listt=[]
        for i in range(n):
            temp=0
            for j in range (n):
                if M[i][j]==0:
                    temp+=1
                if temp==n:
                    listt.append(i)
        if len(listt)!=1:
            return -1
        return listt[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions