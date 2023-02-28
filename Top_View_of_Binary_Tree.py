# This is from Geeks for Geeks.Question link at last
# Given below is a binary tree. 
# The task is to print the top view of binary tree. 
# Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. 
# For the given below tree
#        1
#     /     \
#    2       3
#   /  \    /   \
# 4    5  6   7
# Top view will be: 4 2 1 3 7
# Note: Return nodes from leftmost node to rightmost node. 
# Also if 2 nodes are outside the shadow of the tree and are at same position then consider the extreme ones only(i.e. leftmost and rightmost). 
# For ex - 1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N will give 8 2 1 3 as answer. 
# Here 8 and 9 are on the same position but 9 will get shadowed.
#User function Template for python3
# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        dictt = {}
        q = deque()
        q.append((root, 0))
        while q:
            node,dist = q.popleft()
            if dist not in dictt:
                dictt[dist]=node.data
            if node.left:
                q.append((node.left, dist - 1))
            if node.right:
                q.append((node.right, dist + 1))
        m=[]
        for key in sorted(dictt.keys()):
            m.append(dictt[key])
        t=[]
        for i in m:
                t.append(i)
        return t
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
        ob= Solution()
        
        res = ob.topView(root)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1?page=1&difficulty[]=1&category[]=Tree&sortBy=submissions