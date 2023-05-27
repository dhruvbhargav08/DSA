# This is from Geeks for Geeks.Question link at last
# Given a singly linked list containing N nodes. 
# Modify the Linked list as follows:
# 1. Modify the value of the first half nodes such that 1st node's new value is equal to the value of the last node minus the first node's current value, 2nd node's new value is equal to the second last nodes value minus 2nd nodes current value, likewise for first half nodes.
# 2. Replace the second half of nodes with the initial values of the first half nodes(values before modifying the nodes).
# 3. If N is odd then the value of the middle node remains unchanged.
#User function Template for python3

class Solution:
    def modify_the_list(self, head):
        # code here
        def rev(listt):
            prev=None
            current=listt
            while current is not None:
                nextNode=current.next
                current.next=prev
                prev=current
                current=nextNode
            listt=prev
            return listt
        def helper(temp,lenn):
            head=temp
            listt1=Node(0)
            listt1_head=listt1
            i=1
            while i<(lenn//2+1):
                flag=Node(temp.data)
                listt1.next=flag
                temp=temp.next
                listt1=listt1.next
                i+=1
            listt1=listt1_head.next
            listt2=Node(0)
            listt2_head=listt2
            i=1
            while temp:
                flag=Node(temp.data)
                listt2.next=flag
                temp=temp.next
                listt2=listt2.next
                i+=1
            listt2=listt2_head.next
            listt2=rev(listt2)
            temp=head
            i=1
            while i<(lenn//2+1):
                temp.data=listt2.data-listt1.data
                temp=temp.next
                listt1=listt1.next
                listt2=listt2.next
                i+=1
            if lenn%2:
                temp=temp.next
            i=1
            listt1=listt1_head.next
            listt1=rev(listt1)
            while i<(lenn//2+1):
                temp.data=listt1.data
                temp=temp.next
                listt1=listt1.next
                i+=1
            return head
        def length(temp):
            count=0
            while temp:
                count+=1
                temp=temp.next
            return count
        lenn=length(head)
        listt=helper(head,lenn)
        return listt
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def modify_the_list(head):
    current = head
    while current is not None:
        if current.next is not None and current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


t = int(input())
while t > 0:
    n = int(input())
    linked_list_arr = list(map(int, input().split()))
    head = None
    temp = None
    for a in linked_list_arr:
        new_node = Node(a)
        if head is None:
            head = new_node
        else:
            temp.next = new_node
        temp = new_node
    head = Solution().modify_the_list(head)
    print_list(head)
    t -= 1
# } Driver Code Ends
# Quetion link 
# https://practice.geeksforgeeks.org/problems/modify-linked-list-1-0546/1