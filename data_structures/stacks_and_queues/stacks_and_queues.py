class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        new_top = Node(value, self.top)
        self.top = new_top

    def pop(self):
        if not isinstance(self.top, Node):
            raise EmptyStackException()
        removed = self.top
        self.top = self.top.next
        return removed

    def peek(self):
        if isinstance(self.top, Node):
            return self.top.value
        raise EmptyStackException()

    def is_empty(self):
        if self.top:
            return False
        return True


class Queue:
    def __init__(self, front=None):
        self.front = front
        self.end = end_next = self.front
        while end_next:
            if isinstance(end_next, Node):
                self.end = end_next
                end_next = end_next.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.end = new_node
        else:
            self.end.next = self.end = new_node

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException()
        removed = self.front
        self.front = self.front.next
        return removed

    def peek(self):
        if not self.is_empty():
            return self.front.value
        raise EmptyQueueException()

    def is_empty(self):
        if self.front:
            return False
        return True


class EmptyStackException(AttributeError):
    pass


class EmptyQueueException(AttributeError):
    pass
