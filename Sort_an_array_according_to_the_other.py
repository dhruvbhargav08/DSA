# This is from Geeks for Geeks.Question link at last
# Given two integer arrays A1[ ] and A2[ ] of size N and M respectively. 
# Sort the first array A1[ ] such that all the relative positions of the elements in the first array are the same as the elements in the second array A2[ ].
# See example for better understanding.
# Note: If elements are repeated in the second array, consider their first occurance only.
#User function Template for python3

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        # Your Code Here1
        mapp={}
        for i in range (N):
            if A1[i] not in mapp.keys():
                mapp[A1[i]]=1
            else:
                mapp[A1[i]]+=1
        listt=[]
        i=0
        keys=[]
        for i in range (M):
            while A2[i] in mapp and mapp[A2[i]]!=0:
                listt.append(A2[i])
                mapp[A2[i]]-=1
        for i in mapp.keys():
            if mapp[i]!=0:
                keys.append(i)
        keys.sort()
        for i in keys:
            while mapp[i]!=0:
                listt.append(i)
                mapp[i]-=1
        return listt
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/relative-sorting4323/1?page=1&difficulty[]=1&status[]=unsolved&curated[]=1&sortBy=submissions