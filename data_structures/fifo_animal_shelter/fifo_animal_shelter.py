from data_structures.stacks_and_queues.stacks_and_queues import Stack, EmptyStackException


class Cat:
    pass


class Dog:
    pass


class AnimalShelter:

    def __init__(self):
        self.main_stack = Stack()
        self.helper_stack = Stack()

    def enqueue(self, animal):
        while not isinstance(self.main_stack.peek(), EmptyStackException):
            self.helper_stack.push(self.main_stack.pop())

        self.helper_stack.push(animal)

        while not isinstance(self.helper_stack.peek(), EmptyStackException):
            self.main_stack.push(self.helper_stack.pop())

    def dequeue(self, animal):
        if isinstance(self.main_stack.peek(), EmptyStackException):
            return EmptyStackException()

        saved_animal = None

        while not isinstance(self.main_stack.peek(), EmptyStackException):
            if not saved_animal and isinstance(self.main_stack.peek(), animal):
                saved_animal = self.main_stack.pop()
            else:
                self.helper_stack.push(self.main_stack.pop())

        while not isinstance(self.helper_stack.peek(), EmptyStackException):
            self.main_stack.push(self.helper_stack.pop())

        return saved_animal

    def peek(self):
        return self.main_stack.peek()

if __name__ == "__main__":
    animal_queue = AnimalShelter()
    animal_queue.enqueue(Cat())
    animal_queue.enqueue(Cat())
    animal_queue.enqueue(Dog())
    animal_queue.peek()
