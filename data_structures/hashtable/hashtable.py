class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.length = 1024
        self.size = 0
        self.bucket = [None]*self.length

    def hash(self, key):
        hash_index = 0
        for idx, c in enumerate(key):
            hash_index += (idx + len(key)) ** ord(c)
            hash_index = hash_index % self.length
        return hash_index

    def add(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.bucket[index]
        if node is None:
            self.bucket[index] = Node(key, value)
            return
        prev = node
        while node:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def get(self, key):
        index = self.hash(key)
        node = self.bucket[index]
        while node != None and node.key != key:
            node = node.next
        if not node:
            return None
        else:
            return node.value

    def contains(self, key):
        index = self.hash(key)
        node = self.bucket[index]
        if not node:
            return False
        else:
            return True
