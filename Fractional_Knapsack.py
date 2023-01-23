#This is from Geeks for Geeks.Question link at last
# Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# Note: Unlike 0/1 knapsack, you are allowed to break the item. 
#User function Template for python3

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        # code here
        listt=[]
        total=0
        for i in range(n):
            listt.append([Items[i].value/Items[i].weight,i])
        listt.sort(reverse=True)
        for i in range(n):
            w=Items[listt[i][1]].weight
            if w<W:
                total += Items[listt[i][1]].value
                W-=w
            else:
                total+=W*listt[i][0]
                break
        return total
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions