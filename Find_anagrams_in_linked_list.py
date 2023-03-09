# This is from Geeks for Geeks.Question link at last
#User function Template for python3

class Solution:
    def findAnagrams(self, head, s):
        # code here
        n=len(s)
        a = [0]*26
        for e in s:
            a[ord(e)-ord('a')] += 1
        
        running = [0]*26
        start, end = head, head
        cnt = 0
        ans = []
        while start and end:
            idx = ord(end.data)-ord('a')
            running[idx] += 1
            cnt += 1
            
            if cnt > n:
                idx = ord(start.data)-ord('a')
                running[idx] -=1
                cnt -= 1
                start.next, start = None, start.next
            if running == a:
                end.next, end = None, end.next
                ans.append(start)
                running = [0]*26
                cnt = 0
                start = end
            else:
                end = end.next
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self):
        self.data = None
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        if self.head == None:
            self.head = Node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = Node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next
            
def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(str, input().strip().split()))
        for i in values:
            list1.insert(i)
        s = input()
        res = Solution().findAnagrams(list1.head, s)
        for i in range(len(res)):
            printlist(res[i])
        if len(res) == 0:
            print(-1)
            
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/de6f6a196aecdfb3e4939ba7729809a5a4bdfe90/1