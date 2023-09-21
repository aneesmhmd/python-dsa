class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BST(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BST(val)

    def search(self, val):
        if self.val == val:
            print(f'{val} present in BST')
            return

        if val < self.val:
            if self.left:
                self.left.search(val)
            else:
                print(f'{val} not present in BST')
        else:
            if self.right:
                self.right.search(val)
            else:
                print(f'{val} not present in BST')

    def delete(self, val):
        if self.val is None:
            print('BST is empty')
            return
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            else:
                print(f'{val} not present')
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            else:
                print(f'{val} not present')
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.val = node.val
            self.right = self.right.delete(node.val)
        return self

    def is_valid(self):
        arr = self.inorder()
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

    def pre_order(self):
        print(self.val, end=", ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def inorder(self, arr=[]):
        if self.left:
            self.left.inorder()
        print(self.val, end=", ")
        arr.append(self.val)
        if self.right:
            self.right.inorder()

        return arr

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.val, end=", ")


obj = BST(48)
elements = [3, 4, 7, 13, 7, 134, 13, 45, 145]
for i in elements:
    obj.insert(i)

# print(obj.is_valid())
obj.delete(4)
obj.delete(48)
obj.post_order()
print()