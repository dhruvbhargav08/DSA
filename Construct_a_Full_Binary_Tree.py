# This is from Geeks for Geeks.Question link at last
# Given two arrays that represent Preorder traversals of a Full binary tree preOrder[] and its mirror tree preOrderMirror[], 
# your task is to complete the function constructBinaryTree(), 
# that constructs the full binary tree using these two Preorder traversals.
# Note: It is not possible to construct a general binary tree using these two traversal. 
# But it is possible to create a full binary tree using the above traversals without any ambiguity.
#User function Template for python3
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
class Solution:
    def constructBinaryTree(self, pre, preMirror, size):
        # code here
        def helper(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            node=Node(pre[left])
            node.left=helper(left+1,mid)
            node.right=helper(mid+1,right)
            return node
        root=helper(0,size-1)
        return root


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    def printInorder(node):
        if node == None:
            return
        printInorder(node.left)
        print(node.data, end = " ")
        printInorder(node.right)
        
    test_cases = int(input())
    for _ in range (test_cases):
        N = int(input())
        pre = list(map(int, input().split()))
        preMirror = list(map(int, input().split()))
        res = Solution().constructBinaryTree(pre, preMirror, N)
        if printInorder(res) != None:
            print(printInorder(res)[:len(printInorder(res))-2])
        print()
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/93c977e771fc0d82e87ba570702732edb2226ad7/1