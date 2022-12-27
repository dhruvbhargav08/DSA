# This code display how we can reverse a list using iterative and recursive approach,
# how to check for loop in given linkedlist and 
# how to reverse the list in pair of 2.
class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.headval = None
    def extent(self,data):
        temp=self.headval
        new_Node=Node(data)
        while temp.next is not None:
            temp=temp.next
        temp.next=new_Node
    def iterative_reverse(self):
        prev=None
        current=self.headval
        while current is not None:
            nextNode=current.next
            current.next=prev
            prev=current
            current=nextNode
        self.headval=prev
    def recurssion_reverse(self,prev,curr):
        if curr is not None:
            self.recurssion_reverse(curr,curr.next)
            curr.next=prev
        else:
            self.headval=prev
    def checkloop(self):
        slow=fast=self.headval
        counter=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                print("Contain loop")
                counter+=1
                break
        if counter==0:
            print("No loop exist")
    def reverse_in_pair(self):
        temp1=None
        temp2=None
        curr=self.headval
        while curr!=None and curr.next!=None:
            if temp1!=None:
                temp1.next.next=curr.next
            temp1=curr.next
            curr.next=curr.next.next
            temp1.next=curr
            if temp2==None:
                temp2=temp1
            curr=curr.next
        self.headval=temp2
    def display(self):
        temp=self.headval
        while temp is not None:
            print(temp.data)
            temp=temp.next
list = SingleLinkedList()
list.headval = Node(1)
list.extent(2)
list.extent(3)
list.extent(4)
list.extent(5)
print("Input linkedlist")
list.display()
print("Iterative Reverse")
list.iterative_reverse()
list.display()
print("Recursive Reverse")
list.recurssion_reverse(None,list.headval)
list.display()
print("Checking for loop")
list.checkloop()
list.display()
print("Reverse in pair")
list.reverse_in_pair()
list.display()