#This is from Geeks for Geeks.Question link at last
# Given a linked list of N nodes such that it may contain a loop.
# A loop here means that the last node of the link list is connected to the node at position X(1-based index). 
# If the link list does not have any loop, X=0.
# Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.
'''
# node class:
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        if head is None or head.next is None:
            return head
        temp=head
        link_set=set()
        while temp is not None:
            if temp.next in link_set:
                temp.next=None
                return head
            link_set.add(temp)
            temp=temp.next
        return head
        # remove the loop without losing any nodes
#{ 
 # Driver Code Starts
# driver code:
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val
class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def add(self,num):
        if self.head is None:
            self.head=Node(num)
            self.tail=self.head
        else:
            self.tail.next=Node(num)
            self.tail=self.tail.next
    def isLoop(self):
        if self.head is None:
            return False  
        fast=self.head.next
        slow=self.head  
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast=fast.next.next
            slow=slow.next  
        return True
    def loopHere(self,position):
        if position==0:
            return    
        walk=self.head
        for _ in range(1,position):
            walk=walk.next
        self.tail.next=walk  
    def length(self):
        walk=self.head
        ret=0
        while walk:
            ret+=1
            walk=walk.next
        return ret
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=tuple(int(x) for x in input().split())
        pos=int(input())
        
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)
        
        Solution().removeLoop(ll.head)
        
        if ll.isLoop() or ll.length()!=n:
            print(0)
            continue
        else:
            print(1)
# } Driver Code 
# Question link
# https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions