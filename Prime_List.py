# This is from Geeks for Geeks.Question link at last
# You are given the head of a linked list. 
# You have to replace all the values of the nodes with the nearest prime number. 
# If more than one prime number exists at an equal distance, choose the smallest one.
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
    def primeList(self, head : Optional['Node']) -> Optional['Node']:
        # code here
        listt=[]
        
        def prime(i):
            for j in range (2,int(i**0.5)+1):
                if i%j==0:
                    return False
            return True
        for i in range (2,10008):
            if prime(i):
                listt.append(i)
        temp=head
        while temp:
                j=0
                while temp.data>listt[j]:
                    j+=1
                value1=abs(temp.data-listt[j-1])
                value2=abs(temp.data-listt[j])
                if value1<=value2:
                    temp.data=listt[j-1]
                elif value1>value2:
                    temp.data=listt[j]
                temp=temp.next
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
        
        obj = Solution()
        res = obj.primeList(head)
        
        printList(res)
        

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/6cb0782855c0f11445b8d70e220f888e6ea8e22a/0