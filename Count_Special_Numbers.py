#This is from Geeks for Geeks.Question link at last
# You are given an array arr[ ] of size N consisting of only positive integers. 
# Your task is to find the count of special numbers in the array. 
# A number is said to be a special number if it is divisible by at least 1 other element of the array.
#User function Template for python3

class Solution:
    def countSpecialNumbers(self, N, arr):
        # Code here
        count=0
        dictt={}
        sett=set()
        set_len=0
        special=set()
        for i in range (N):
            if arr[i] in sett:
                dictt[arr[i]]+=1
            else:
                dictt[arr[i]]=1
                sett.add(arr[i])
                set_len+=1
        maxx=max(arr)
        for i in sett:
            j=i*2
            while j<=maxx:
                if j in sett:
                    special.add(j)
                j+=i
        for i in sett:
            if dictt[i]>1:
                count+=dictt[i]
            elif i in special:
                count+=1
        return count
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.countSpecialNumbers(N, arr))
        
        T -= 1
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/3d49e4cce2820a813da02d1587c2dd9c542ce769/1