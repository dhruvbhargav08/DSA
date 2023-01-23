#This is from Geeks for Geeks.Question link at last
# Given two sorted linked lists consisting of N and M nodes respectively. 
# The task is to merge both of the list (in-place) and return head of the merged list.
#User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to merge two sorted linked list.
def sortedMerge(head1, head2):
    # code here
    new=LinkedList()
    temp1=head1
    temp2=head2
    while temp1!=None or temp2!=None:
        if temp1!=None and temp2!=None:
            if temp1.data<=temp2.data:
                new.append(temp1.data)
                temp1=temp1.next
            elif temp2.data<temp1.data:
                new.append(temp2.data)
                temp2=temp2.next
        if temp1==None and temp2!=None:
            new.append(temp2.data)
            temp2=temp2.next
        if temp2==None and temp1!=None:
            new.append(temp1.data)
            temp1=temp1.next
    return new.head

#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        for x in nodes_b:
            b.append(x)
        
        printList(sortedMerge(a.head,b.head))

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions