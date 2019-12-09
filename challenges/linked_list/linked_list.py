class Node:

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{self.value} - {self.next}'

    def __str__(self):
        return f'The current node has a value {self.value}, and the next node is {self.next}'

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        old_start_node = self.head
        new_start_node = Node(value, old_start_node)
        self.head = new_start_node

    def includes(self, value):

        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()

        return False

    def to_string(self):
        output = ''
        node = self.head

        while node != None:
            output += f'{node.get_value()} '
            node = node.get_next()

        return output.strip()





