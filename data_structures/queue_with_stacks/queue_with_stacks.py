from data_structures.stacks_and_queues.stacks_and_queues import Node, Stack, EmptyQueueException

class PseudoQueue:
    def __init__(self, stack1):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):

        self.stack1.push(value)

    def dequeue(self):

        if self.stack1.top == None:
            raise EmptyQueueException()
        while self.stack1.top != None:
            popped_value = self.stack1.pop()

            self.stack2.push(popped_value)

        stack2_popped = self.stack2.pop()

        while self.stack2.top != None:
            self.stack1.push(self.stack2.pop())
        return stack2_popped

    def peek(self):
        return self.stack1.peek()

