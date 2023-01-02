#This is from Geeks for Geeks.Question link at last
# Given a Binary Tree. 
# Return true if, for every node X in the tree other than the leaves, its value is equal to the sum of its left subtree's value and its right subtree's value. 
# Else return false.
# An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0. A leaf node is also considered a Sum Tree.
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return True is Tree is SumTree else return False
class Solution:
    def isSumTree(self,root):
        # Code here
        if root==None:
            return 0
        return root.data+self.sum_tree(root.left)+self.sum_tree(root.right)
    def isSumTree(self,root):
        # Code here
        if root==None:
            return True 
        if root and root.left==None and root.right==None:
            return True
        left=self.sum_tree(root.left)
        right=self.sum_tree(root.right)
        if root.data==left+right and self.isSumTree(root.left) and self.isSumTree(root.right):
            return True 
        else:
            return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Contributed by Sudarshan Sharma
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
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        if Solution().isSumTree(root):
            print(1) 
        else:
            print(0)
# } Driver Code Ends
#Question link
# https://practice.geeksforgeeks.org/problems/sum-tree/1?page=1&difficulty[]=1&status[]=solved&category[]=Tree&sortBy=submissions
