class Node:
    def __init__(self, key):
        self.value = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = self.tail = None

    def print_list(self):
        if self.length > 0:
            curr = self.head
            while curr:
                print(curr.value, end='-')
                curr = curr.next
            print()

    def add_at_end(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def add_at_start(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def value_exists(self, data) -> bool:
        if self.length == 0:
            return False
        if self.head.value == data or self.tail.value == data:
            return True
        curr = self.head
        while curr.next:
            if curr.next.value == data:
                return True
            curr = curr.next
        return False

    def pop_head(self):
        if self.length <= 1:
            self.head = self.tail = None
            self.length = 0
            return
        self.head = self.head.next
        self.length -= 1

    def pop_tail(self):
        if self.length <= 1:
            self.head = self.tail = None
            self.length = 0
        curr = self.head
        for _ in range(self.length - 2):
            curr = curr.next
        curr.next = None
        self.tail = curr
        self.length -= 1

    def delete_value(self, data):
        if self.length > 0:
            if self.head.value == data:
                self.pop_head()
            elif self.tail.value == data:
                self.pop_tail()
            else:
                curr = self.head
                while curr.next:
                    if curr.next.value == data:
                        curr.next = curr.next.next
                        return
                    curr = curr.next


myList = LinkedList()
myList.add_at_end(1)
myList.add_at_end(5)
myList.add_at_end(8)
myList.add_at_end(12)
myList.add_at_end(90)
myList.add_at_end(77)
myList.add_at_end(50)
myList.pop_head()
myList.pop_tail()
myList.delete_value(90)
myList.print_list()
print(myList.value_exists(77))
