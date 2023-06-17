# This is from Geeks for Geeks.Question link at last
# Given N integers, the task is to insert those elements in the queue. 
# Also, given M integers, the task is to find the frequency of each number in the Queue.
# Note:
# insert() will be called N times by main().
# findFrequency() will be called M times by main();
# Where k is each element passing through respective function calls.
#User function Template for python3
class Solution:
    # Function to insert element into the queue
    def insert(self, q, k): 
        #code here
        q.append(k)
    # Function to find frequency of an element
    # return the frequency of k
    def findFrequency(self, q, k):
        # code here
        count =0
        for i in q :
            if i==k:
                count+=1
        return count 
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        obj = Solution()
        q = []
        n = int(input())
        arr = list(map(int, input().strip().split()));
        for k in arr:
            obj.insert(q,k)
        
        
        m = int(input())
        query = list(map(int, input().strip().split()));
        for k in query:
            f = obj.findFrequency(q,k)
            if f!=0:
                print(f)
            else:
                print(-1)

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/queue-operations/1