#This is from Geeks for Geeks.Question link at last
# Given a singly linked list of size N. 
# The task is to left-shift the linked list by k nodes, where k is a given positive integer smaller than or equal to length of the linked list.
# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        temp=head
        while k!=1:
            temp=temp.next
            k-=1
        if temp.next==None:
            return head
        flag=temp.next
        new_=temp.next
        temp.next=None
        while new_.next:
            new_=new_.next
        new_.next=head
        return flag
        



#{ 
 # Driver Code Starts
# driver

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = Solution().rotate(lis.head,k)
        printList(head)
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions