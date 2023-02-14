# This is from Geeks for Geeks.Question link at last
# You are given N number of books. 
# Every ith book has Ai number of pages. 
# You have to allocate contiguous books to M number of students. 
# There can be many ways or permutations to do so. 
# In each permutation, one of the M students will be allocated the maximum number of pages. 
# Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated to a student is the minimum of those in all the other permutations and print this minimum value.
# Each book will be allocated to exactly one student. Each student has to be allocated at least one book.
# Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).
class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        low=min(A)
        high=sum(A)
        res=-1
        def ispossible(A,mid,M):
            n=len(A)
            pagecount=0
            student=1
            for i in range(n):
                if pagecount+A[i]<=mid:
                    pagecount+=A[i]
                else:
                    student+=1
                    if student>M or arr[i]>mid:
                        return False
                    pagecount=A[i]
            return True
        if M>N:
            return -1
        while low<=high:
            mid=(low+high)//2
            if ispossible(A,mid,M):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
    
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/0