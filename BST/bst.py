class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    
    def search(self, data):
        if self.key == data:
            print(f'{data} present in the tree')
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print(f'{data} is not present in the tree')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print(f'{data} is not present in the tree')

    def pre_order(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.in_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key, end=" ")

    def min(self):
        curr = self 
        while curr.lchild:
            curr = curr.lchild
        print('Minimum ', curr.key)

       
list1 = [10,3,45,22,7,1]

root = BST(40)
for i in list1:
    root.insert(i)

root.search(30)
root.search(33)
print('Pre-order')
root.pre_order()

print('\nin-order')
root.in_order()

print('\npost-order')
root.post_order()
print('Minimum')
root.min()