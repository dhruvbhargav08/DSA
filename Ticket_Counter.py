# This is from Geeks for Geeks.Question link at last
# N people from 1 to N are standing in the queue at a movie ticket counter. 
# It is a weird counter, as it distributes tickets to the first K people and then the last K people and again first K people and so on, once a person gets a ticket moves out of the queue. 
# The task is to find the last person to get the ticket.
class Solution:
    def distributeTicket(self, N : int, k : int) -> int:
        # Code Here
        i,j=1,N
        front=True
        while i<=j:
            if front:
                i+=k
                ans=j
            else:
                j-=k
                ans=i
            front=not front
        return ans 
            

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    
    N, K = map(int, input().split())
    
    obj = Solution()
    res = obj.distributeTicket(N, K)
    
    print(res)
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/ticket-counter-2731/1