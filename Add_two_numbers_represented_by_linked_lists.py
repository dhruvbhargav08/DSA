#This is from Geeks for Geeks.Question link at last
# Given two decimal numbers represented by two linked lists of size N and M respectively. 
# The task is to return a linked list that represents the sum of these two numbers.
# For example, the number 190 will be represented by the linked list, 1->9->0->null, similarly 25 by 2->5->null. 
# Sum of these two numbers is 190 + 25 = 215, which will be represented by 2->1->5->null. 
# You are required to return the head of the linked list 2->1->5->null.
#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def lreverse(self,listt):
        prev=None
        current=listt
        while current is not None:
            nextNode=current.next
            current.next=prev
            prev=current
            current=nextNode
        listt=prev
        return listt
    def addTwoLists(self, first, second):
        # code here
        first=self.lreverse(first)
        second=self.lreverse(second)
        listt=Node(1000)
        temp=listt
        carry=0
        while first and second:
            new=Node((first.data+second.data+carry)%10)
            carry=(first.data+second.data+carry)//10
            temp.next=new
            temp=new
            first=first.next
            second=second.next
        if first :
            while first:
                new=Node((first.data+carry)%10)
                carry=(first.data+carry)//10
                temp.next=new
                temp=new
                first=first.next
        if second:
            while second :
                new=Node((second.data+carry)%10)
                carry=(second.data+carry)//10
                temp.next=new
                temp=new
                second=second.next
        if carry>0:
            new=Node(carry)
            temp.next=new
        temp=listt.next
        return self.lreverse(temp)
        # return head of sum list


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1?page=1&category[]=Linked%20List&sortBy=submissions