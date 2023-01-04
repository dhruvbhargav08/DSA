#This is from Geeks for Geeks.Question link at last
# Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. 
# The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. 
# The order of nodes in DLL must be same as Inorder of the given Binary Tree. 
# The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.
# Note: H is the height of the tree and this space is used implicitly for the recursion stack.
#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self,root):
        # do Code here
        temp=Node(0)
        flag=temp
        prev=None
        def inorder(root):
            nonlocal temp,prev
            if root:
                inorder(root.left)
                temp.right=Node(root.data)
                temp=temp.right
                temp.left=prev
                prev=temp
                inorder(root.right)
        inorder(root)
        return flag.right
#{ 
 # Driver Code Starts
#Initial template for Python
from collections import deque
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
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


import sys            
def printDLL(head): #Print util function to print Linked List
    prev = None
    sys.stdout.flush()
    while(head != None):
        print(head.data, end=" ")
        prev=head
        head=head.right
    print('')
    while(prev != None):
        print(prev.data, end=" ")
        prev=prev.left
    print('')
    
if __name__=='__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        head = ob.bToDLL(root)
        printDLL(head)
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/binary-traee-to-dll/0