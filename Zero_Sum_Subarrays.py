# This is from Geeks for Geeks.Question link at last
# You are given an array arr[] of size n. 
# Find the total count of sub-arrays having their sum equal to 0.
#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        #return: count of sub-arrays having their sum equal to 0
        def nc2(n):
            n=n*(n-1)//2
            return n
        dictt={}
        count=0
        summ=0
        for i in range (n):
            summ+=arr[i]
            if summ not in dictt:
                dictt[summ]=0
            dictt[summ]+=1
            if summ==0:
                count+=1
        for i in dictt:
            count+=nc2(dictt[i])
        return count 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/zero-sum-subarrays1825/1?page=1&difficulty[]=1&status[]=unsolved&curated[]=1&sortBy=submissions