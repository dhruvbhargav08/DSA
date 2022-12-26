class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None
def preorder_iterative_traversal(root):
    if root:
        stack=[]
        stack.append(root)
        while len(stack)>0:
            node=stack.pop()
            print(node.val,end=' ')
            if node.right!=None:
                stack.append(node.right)
            if node.left!=None:
                stack.append(node.left) 
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
preorder_iterative_traversal(root)

    