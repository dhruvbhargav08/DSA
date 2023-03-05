# This is from Geeks for Geeks.Question link at last
# Given a linked list and a number k. 
# You have to reverse first part of linked list with k nodes and the second part with n-k nodes.

from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""

class Solution:
    def lreverse(self,listt,k):
        prev=None
        current=listt
        num=0
        while current is not None:
            if num==k:
                break
            nextNode=current.next
            current.next=prev
            prev=current
            current=nextNode
            num+=1
        listt=prev
        return listt
    def reverse(self, head : Optional['Node'], k : int) -> Optional['Node']:
        # code here
        temp,i=head,0
        n=0
        while temp:
            n+=1
            temp=temp.next
        temp=head
        while temp and i<k:
            i+=1
            temp=temp.next
        head=self.lreverse(head,k)
        temp=self.lreverse(temp,n-k)
        flag=head
        while flag.next:
            flag=flag.next
        flag.next=temp
        return head
        
        



#{ 
 # Driver Code Starts

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

def printList(node):
    while (node != None):
        print(node.data,end=" ")
        node = node.next
    print()
def inputList():
    n=int(input())#lenght of link list
    data=[int(i) for i in input().strip().split()]#all data of linked list in a line
    head = Node(data[0])
    tail = head;
    for i in range(1,n):
        tail.next = Node(data[i]);
        tail = tail.next;
    return head;

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        head = inputList()
        
        
        k = int(input())
        
        obj = Solution()
        res = obj.reverse(head, k)
        
        printList(res)
        

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/bae68b4d6a2a77fb6bd459cf7447240919ebfbf5/1