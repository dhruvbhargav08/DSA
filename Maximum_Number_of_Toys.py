#This is from Geeks for Geeks.Question link at last.
# You are given N toys in a shop .
# The cost of each toy is represented by an array A[]. 
# You are given Q queries, For ith query, You have a C amount of money which you can use to purchase the toys. 
# Also there are K broken toys and you won't purchase them. 
# The task is to calculate the maximum number of toys you can purchase using the C amount of money.
# Note: 1 based indexing is used. Each query is treated independently. 
# Query definition: The first element represents an integer C where C=Queries[i][0].
# The second element represents an integer K, where K = Queries[i][1].
# The next K integers represent the indices of broken toys which are Queries[i][j] ,j>1

#User function Template for python3

import sys
class Solution:
    def Sort(self,A):
        arr=A.sort()
        return arr
    def maximumToys(self,N,A,Q,Queries):
      #code here
        res=[0]*Q
        listt=sorted(A)
        for i in range (Q):
            temp=listt.copy()
            cost=Queries[i][0]
            for j in range (Queries[i][1]):
                temp.remove(A[Queries[i][j+2]-1])
            summ=0
            count=0
            for j in range (N-Queries[i][1]):
                summ+=temp[j]
                if summ<=cost :
                    count+=1
            res[i]=count
        return res

                




#{ 
 # Driver Code Starts


for _ in range(int(input())):
    N=int(input())
    A=[int(i) for i in input().strip().split()]
    Q=int(input())
    Queries=[[] for i in range(Q)]
    for i in range(Q):
        Queries[i].extend(int(i) for i in input().strip().split())
    obj=Solution()
    ans=obj.maximumToys(N,A,Q,Queries)
    for i in ans:
        print(i,end=" ")
    print()
    


# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/maximum-number-of-toys/0