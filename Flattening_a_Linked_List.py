#This is from Geeks for Geeks.Question link at last
# Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
# (i) a next pointer to the next node,
# (ii) a bottom pointer to a linked list where this node is head.
# Each of the sub-linked-list is in sorted order.
# Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
# Note: The flattened list will be printed using the bottom pointer instead of next pointer.
#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
class Solution():
    def merge(self,root1,root2):
        temp=Node(0)
        newnode=temp
        while root1 and root2:
            if root1.data<root2.data:
                newnode.bottom=root1
                root1=root1.bottom
            else:
                newnode.bottom=root2
                root2=root2.bottom
            newnode=newnode.bottom
        if root1:
            newnode.bottom=root1
        if root2:
            newnode.bottom=root2
        return temp.bottom
    def flatten(self,root):
        #Your code here
        if not root:
            return None
        if not root.next:
            return root
        return self.merge(root,self.flatten(root.next))
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
        

def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
        
    print()


if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]
        
        arr=[int(x) for x in input().strip().split()]
        temp=None
        tempB=None
        pre=None
        preB=None
        
        flag=1
        flag1=1
        listo=[int(x) for x in input().strip().split()]
        it=0
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag is 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1
                
            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 is 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        obj=Solution()
        root=obj.flatten(head)
        printList(root)
        
        t-=1
            
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/da62a798bca208c7a678c133569c3dc7f5b73500/1