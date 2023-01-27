# This is from Geeks for Geeks.Question link at last
# Given a binary tree and a node called target. 
# Find the minimum time required to burn the complete binary tree if the target is set on fire. 
# It is known that in 1 second all nodes connected to a given node get burned. 
# That is its left child, right child, and parent.
#User function Template for python3

class Solution:
    def minTime(self, root,target):
        # code here
        def findnode(root): 
            if root == None:
                return None
            if root.data == target:
                return root
            return findnode(root.left) or findnode(root.right)
        node=findnode(root)
        def parent_check(): 
            que = deque()
            que.append(root)
            while que:
                node = que.popleft()
                if node.left != None:
                    parent[node.left] = node
                    que.append(node.left)
                if node.right != None:
                    parent[node.right] = node
                    que.append(node.right)
        parent = {}
        parent_check()
        visited=[]
        ans = 0
        queue=deque()
        queue.append(node)
        visited.append(node)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left != None and node.left not in visited:
                    queue.append(node.left)
                    visited.append(node.left)
                if node.right != None and node.right not in visited:
                    queue.append(node.right)
                    visited.append(node.right)
                if node in parent and parent[node] not in visited:
                    queue.append(parent[node])
                    visited.append(parent[node])
            ans += 1
        return ans-1

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
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/burning-tree/0