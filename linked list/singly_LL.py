class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data, '--->', end=" ")
                n = n.ref

    # < --------Insertion-------- >
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linked list is not empty')

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        if self.head is None:
            print('Linked List is empty')
            return
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref

        if n is None:
            print('Given node is not present in the Linked List')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print('Linked List is empty')
            return
        new_node = Node(data)
        n = self.head
        if n.data == x:
            new_node.ref = n
            n = new_node
            return

        while n is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n is None:
            print(x, " is not present in the Linked List")
        else:
            new_node.ref = n.ref
            n.ref = new_node

    # < --------Deletion-------- >
    def delete_begin(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def del_by_value(self, x):
        if self.head is None:
            print("LL is empty")
        elif self.head.data == x:
            self.head = self.head.ref
        else:
            n = self.head
            while n is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            n.ref = n.ref.ref

    def find_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr is not None and fast_ptr.ref is not None:
            slow_ptr = slow_ptr.ref
            fast_ptr = fast_ptr.ref.ref
        print('Middle element is :',slow_ptr.data)


L1 = LinkedList()

L1.insert_empty(11)
L1.add_begin(10)
L1.add_after(13, 11)
L1.add_before(12, 13)
L1.add_end(14)
# L1.delete_begin()
# L1.delete_end()
# L1.del_by_value(13)
L1.find_middle()
L1.print_LL()
