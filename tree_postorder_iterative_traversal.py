# A python program for tree postorder traversal using iterative approach.
class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None
def peek(stack):
        if len(stack) > 0:
            return stack[-1]
        return None
def postorder_iterative_traversal(root):
    stack=[]
    while True:
        while root:
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root=root.left
        root=stack.pop()
        if (root.right!=None) and (peek(stack)==root.right):
            stack.pop()
            stack.append(root)
            root=root.right
        else:
            print(root.val,end=' ')
            root=None
        if len(stack)<=0:
            break
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
postorder_iterative_traversal(root)

    
