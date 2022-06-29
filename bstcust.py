class Nodebst:
    def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

    def insert(self,data):

#comparison between new value with the parent node
        if self.data:
           if data < self.data:
                if self .left is None:
                   self.left = Nodebst(data)

                else:
                  self.left.insert(data)

           elif data > self.data:
                if self.right is None:
                   self.right = Nodebst(data)
                else:
                   self.right.insert(data)

        else :
            self.data = data

#print the Tree

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

#inorderTravelsal
#left>root>right
    def inorderTravelsal(left,root):
        res = []
        if root:
            res = self.inorderTravelsal(root.left)
            res.append(root.data)
            res = res + self.inorderTravelsal(root.right)
        return res

#search function BST
    def searchBST(self, data):
        
        if self.data == data:
            print('item is found')
            return
        if data < self.data:
            if self .left:
               self.left.searchBST(data)
               return
            else:
                print('item doesnot available')
        else:
            if self.right:
               self.right.searchBST(data)
               return
            else:
                print('the item doesnot exist')
