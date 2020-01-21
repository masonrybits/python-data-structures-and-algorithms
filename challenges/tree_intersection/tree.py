from collections import deque


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def is_empty(self):
        return len(self.dq) == 0


class Tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = self.Node(value)
            return
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            current = q.dequeue()
            if current.left:
                q.enqueue(current.left)
            else:
                current.left = self.Node(value)
            if current.right:
                q.enqueue(current.right)
            else:
                current.right = self.Node(value)
