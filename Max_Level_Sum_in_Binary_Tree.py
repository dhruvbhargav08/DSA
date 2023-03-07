#This is from Geeks for Geeks.Question link at last
# Given a Binary Tree having positive and negative nodes. 
# Find the maximum sum of a level in the given Binary Tree.
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    

# } Driver Code Ends
# Your task is to complete this function
# function should return max sum level in the tree
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
class Solution:
    def maxLevelSum(self, root):
        # Code here
        queue=[]
        res=[]
        queue.append(root)
        while len(queue)>0:
            n=len(queue)
            listt=queue
            summ=0
            for i in range (n):
                node=listt.pop(0)
                summ+=node.data
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(summ)
        # print(res)
        return max(res)
        

#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        s=input()
        root=buildTree(s)
        print(Solution().maxLevelSum(root))

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/4b7ff87c26ed23b3f63c25c611690213d44fb6aa/1