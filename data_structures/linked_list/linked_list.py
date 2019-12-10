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

    def append(self, value):
        new_node = Node(value, None)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def insert_before(self, value, new_value):
        current = self.head
        previous = current

        while current:
            if current.value == value:
                new_node = Node(new_value, None)
                new_node.next = current
                previous.next = new_node
                return
            previous = current
            current = current.next
        else:
            return 'No such as value in the list.'

    def insert_after(self, value, new_value):
        current = self.head
        while current:
            if current.value == value:
                new_node = Node(new_value,None)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        else:
            return 'No such as value in the list.'


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    ll.insertAfter(99)
    print(ll.to_string())







