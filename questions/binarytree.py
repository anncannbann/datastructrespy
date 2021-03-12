#To implement binary tree,
# things i need to add: add,insert,delete
#       def add(root,val)
#       def insert(root,level,val)
#       def del(val,root)

# topmmost node = root ,below are children


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def PrintTree(self):
        # print(self.val)
        if (not self.data):
            return 
        if self.left:
                self.left.PrintTree()
        print(self.data,end=" ")
        if self.right:
                self.right.PrintTree()
        #print(self.data)

    def add(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.add(data)
        else:
            self.data = data

    def delete(self,data):
        if (not self.data):
            return None
        


#main
root = Node(1)
root.left = Node(11) 
root.left.left = Node(7) 
root.left.right = Node(12) 
root.right = Node(9) 
root.right.left = Node(15) 
root.right.right = Node(8) 
root.add(4)

root.PrintTree()