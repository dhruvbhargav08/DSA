# This is from Geeks for Geeks.Question link at last.
# Given a binary tree, find its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def maxDepth(self,root):
        flag=1
        depth=0
        def helper(node,flag):
            nonlocal depth
            if flag>depth:
                depth=flag
            if node.left:
                helper(node.left,flag+1)
            if node.right:
                helper(node.right,flag+1)
        helper(root,flag)
        return depth
    

#{ 
 # Driver Code Starts.

from collections import defaultdict
from collections import deque
from sys import stdin, stdout
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

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        s= input()
        root = buildTree(s)
        
        res = Solution().maxDepth(root)
        print(res)

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/maximum-depth-of-binary-tree/1