class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def show(self):
        node = self.head
        while node:
            print(node.data, ' -> ', end='')
            node = node.next

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __getitem__(self, item):
        node = self.head
        count = 0
        while node:
            if count == item:
                return node
            count += 1
            node = node.next



