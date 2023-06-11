# This is from Geeks for Geeks.Question link at last
# You start with an array A of size N. 
# Initially all elements of the array A are zero. 
# You will be given K positive integers. 
# Let j be one of these integers, you have to add 1 to all A[i], where i ≥ j. 
# Your task is to print the array A after all these K updates are done.
# Note: 1-based indexing is used everywhere in this question.
#User function Template for python3

class Solution:
    def update(self, a, n, updates, k):
        # Your code goes here
        summ=0
        for i in range (k):
            a[updates[i]-1]+=1
        for i in range (n):
            a[i]+=summ
            summ=a[i]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n , k = sz[0] , sz[1]
        a = [0 for i in range(n)]
        updates = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.update(a, n, updates, k)
        print(*a)

        T -= 1


# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/adding-ones3628/1