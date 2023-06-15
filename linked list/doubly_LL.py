class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="<--->")
                n = n.next

    def print_LL_reverse(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n.prev is not None:
                print(n.data, end="<--->")
                n = n.prev
            print()

    def add_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('LL is not empty')

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n

    def add_after(self, data, val):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == val:
                    break
                n = n.next

            if n is None:
                print(val, ' is not present in the Linked List')
            else:
                new_node = Node(data)
                new_node.next = n.next
                new_node.prev = n
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    def add_before(self, data, val):
        if self.head is None:
            print('LL is empty')
        else:
            n = self.head
            while n is not None:
                if n.data == val:
                    break
                n = n.next

            if n is None:
                print(val, ' is not present in the Linked List')
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                else:
                    self.head = new_node
                n.prev = new_node

    def del_begin(self):
        if self.head is None:
            print('LL is empty')
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def del_end(self):
        if self.head is None:
            print('LL is empty')
            return
        if self.head.next is None:
            self.head = None
            return

        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None
        n.prev = None

    def del_by_value(self, val):
        if self.head is None:
            print('LL is empty')
            return
        if self.head.data == val:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return

        n = self.head
        while n.next is not None:
            if n.next.data == val:
                break
            n = n.next

        if n is None:
            print(val, 'is not present in the Linked List')
        else:
            n.next = n.next.next
            if n.next is not None:
                n.next.prev = n


linked = DoublyLinkedList()
linked.add_begin(12)
linked.add_before(10, 12)
linked.add_after(11, 10)
linked.add_end(13)
linked.del_by_value(13)
linked.print_LL()
