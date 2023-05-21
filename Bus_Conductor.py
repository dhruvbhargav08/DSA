# This is from Geeks for Geeks.Question link at last
# You are conductor of a bus.
# There are n chairs and n passengers in the bus. 
# You are given an array chairs of length n, where chairs[i] is the position of the ith chair. 
# You are also given the array passengers of length n, where passengers[j] is the position of the jth passenger.
# You may perform the following move any number of times:
# Increase or decrease the position of the ith passenger by 1 (i.e., moving the ith passenger from position x to x + 1 or x - 1)
# Return the minimum number of moves required to move each passenger to a chair such that no two passengers are in the same chair and every passenger gets a chair.
# Note that there may be multiple chairs or passengers in the same position at the beginning.
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def findMoves(self,n,chairs,passengers):
        #code here
        chairs.sort()
        passengers.sort()
        count=0
        for i in range (n):
            count+=abs(chairs[i]-passengers[i])
        return count 
        
        

#{ 
 # Driver Code Starts.
if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        a=[int(i) for i in input().split()]
        b=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.findMoves(n,a,b))
        
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/c6ced401352fd126b89129cd562a9247f057e40e/1