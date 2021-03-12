#To implement binary tree,
# things i need to add: add,insert,delete
#       def add(root,val)
#       def insert(root,level,val)
#       def del(val,root)

# topmmost node = root ,below are children


class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
    
    def PrintTree(self):
        print(self.val)
        
        if(self.left!=0):
            print(root.left.val)
        if(self.right!=0):
            print(root.right.val)



#main
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.right.left = Node(5)
root.left.right = Node(10)
root.PrintTree()