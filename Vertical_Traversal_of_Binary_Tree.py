# This is from Geeks for Geeks.Question link at last
# Given a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
# If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.
#User function Template for python3


class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        dictt = {}
        q = deque()
        q.append((root, 0))
        while q:
            node,dist = q.popleft()
            if dist not in dictt:
                dictt[dist]=[]
            dictt[dist].append(node.data)
            if node.left:
                q.append((node.left, dist - 1))
            if node.right:
                q.append((node.right, dist + 1))
        m=[]
        for key in sorted(dictt.keys()):
            m.append(dictt[key])
        t=[]
        for i in m:
            for j in i:
                t.append(j)
        return t


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
    import sys
    sys.setrecursionlimit(10000)
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = Solution().verticalOrder(root)
        for i in res:
            print (i, end=" ")
        print()



# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1?page=1&difficulty[]=1&category[]=Tree&sortBy=submissions