from collections import deque


class BinaryTree:
    """Simple BinaryTree with enough functionality for breadth first adding"""

    def __init__(self):
        self._root = None

    def add(self, value):

        node = _Node(value)

        if not self._root:
            self._root = node
            return

        q = Queue()

        q.enqueue(self._root)

        while not q.is_empty():

            current = q.dequeue()

            if current.left:
                q.enqueue(current.left)
            else:
                current.left = node
                break

            if current.right:
                q.enqueue(current.right)
            else:
                current.right = node
                break

    def breadth_first(self):
        if not self._root:
            return []
        new_list = []
        q = Queue()
        q.enqueue(self._root)
        while not q.is_empty():
            current = q.dequeue()
            new_list.append(current.value)
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
        return new_list


class _Node:
    """Protected Tree Node"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Queue:
    """Implementation of Queue that "composes" built in deque class"""

    def __init__(self):
        self._dq = deque()

    def enqueue(self, value):
        self._dq.appendleft(value)

    def dequeue(self):
        return self._dq.pop()

    def peek(self):
        return self._dq[-1]

    def is_empty(self):
        return len(self._dq) == 0
