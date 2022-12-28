# A python program for tree inorder traversal using iterative approach.
class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None
def inorder_iterative_traversal(root):
    if root:
        stack=[]
        temp=root
        while True:
            if temp is not None:
                stack.append(temp)
                temp=temp.left
            elif stack:
                flag=stack.pop()
                print(flag.val,end=' ')
                temp=flag.right
            else:
                break
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
inorder_iterative_traversal(root)

    
