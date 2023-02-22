#This is from Geeks for Geeks.Question link at last
# Given a binary tree, connect the nodes that are at the same level. 
# The structure of the tree Node contains an addition nextRight pointer for this purpose.
# Initially, all the nextRight pointers point to garbage values. 
# Your function should set these pointers to point next right for each node.
#User function Template for python3


'''
:param root: root of the given tree
:return: none, just connect accordingly.
{
    # Node Class:
    class Node:
        def __init__(self,val):
            self.data = val
            self.left = None
            self.right = None
            self.nextRight = None
}
'''

class Solution:
    def connect(self, root):
        # code here
        listt=[root]
        prev=root
        while len(listt)>0:
            temp=listt.copy()
            n=len(temp)
            for i in range(n):
                node=listt.pop(0)
                if node==prev:
                    pass
                if node!=prev and i!=0:
                    prev.nextRight=node
                    prev=node
                if i==0:
                    prev=node
                if node.left:
                    listt.append(node.left)
                if node.right:
                    listt.append(node.right)
        return root



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
        self.nextRight = None
    
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
    


def InOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated in order Traversal of the given tree.
    '''
    if root is None: # check if the root is none
        return
    InOrder(root.left) # do in order of left child
    print(root.data, end=" ")  # print root of the given tree
    InOrder(root.right) # do in order of right child

def printSpecial(root):
    leftmost_node = root

    while leftmost_node :
        curr_node = leftmost_node
        leftmost_node = None
        if curr_node.left :
            leftmost_node = curr_node.left
        elif curr_node.right :
            leftmost_node = curr_node.right

        print(curr_node.data,end=" ")
        curr_node=curr_node.nextRight
        while curr_node:
            print(curr_node.data,end=" ")
            if leftmost_node==None:
                if curr_node and curr_node.left:
                    leftmost_node=curr_node.left
            if leftmost_node==None:
                if curr_node and curr_node.right:
                    leftmost_node=curr_node.right
                
            curr_node = curr_node.nextRight
    print()


    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        obj = Solution();
        obj.connect(root)
        printSpecial(root)
        InOrder(root)
        print()
        
        

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/95423710beef46bd66f8dbb48c510b2c320dab05/1