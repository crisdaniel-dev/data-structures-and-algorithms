from node import Node

class Singly:

    def __init__(self):
        self.__head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node

    def add_last(self, data):
        new_node = Node(data)

        if not self.__head:
            self.__head = new_node
            return

        current = self.__head
        while current.next:
            current = current.next

        current.next = new_node

    def front(self):
        if not self.__head:
            return None
        return self.__head.data

    def rear(self):
        if not self.__head:
            return None

        current = self.__head
        while current.next:
            current = current.next

        return current.data

    def add_before(self, target, data):
        if not self.__head:
            return

        if self.__head.data == target:
            new_node = Node(data)
            new_node.next = self.__head
            self.__head = new_node
            return

        current = self.__head

        while current.next:
            if current.next.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def add_after(self, target, data):
        current = self.__head

        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def del_first(self):
        if not self.__head:
            return

        self.__head = self.__head.next

    def del_last(self):
        if not self.__head:
            return

        if not self.__head.next:
            self.__head = None
            return

        current = self.__head

        while current.next.next:
            current = current.next

        current.next = None

    def display(self):
        if not self.__head:
            return "Empty"

        current = self.__head
        result = ""

        while current:
            result += str(current.data)

            if current.next:
                result += " -> "

            current = current.next

        return result
