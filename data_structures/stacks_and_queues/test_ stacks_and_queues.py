from stacks_and_queues import Node, Stack, Queue


def test_stack_push():
    testing_stack = Stack()
    testing_stack.push(2)
    expected = 2
    actual = testing_stack.peek()
    assert actual == expected


def test_stack_pop():
    testing_stack = Stack()
    testing_stack.push(1)
    testing_stack.push(2)
    expected = 2
    actual = testing_stack.peek()
    assert actual == expected


def test_stack_peek():
    testing_stack = Stack()
    testing_stack.push('hello')
    expected = 'hello'
    actual = testing_stack.peek()
    assert actual == expected


def test_stack_is_empty():
    testing_stack = Stack()
    expected = True
    actual = testing_stack.is_empty()
    assert actual == expected


def test_queue_enque():
    testing_queue = Queue()
    testing_queue.enque(1)
    testing_queue.enque(2)
    expected = 1
    actual = testing_queue.peek()
    assert actual == expected


def test_queue_deque():
    testing_queue = Queue()
    testing_queue.enque(1)
    testing_queue.enque(2)
    testing_queue.deque()
    expected = 2
    actual = testing_queue.peek()
    assert actual == expected


def test_queue_peek():
    testing_queue = Queue()
    testing_queue.enque('hello')
    testing_queue.enque('hallo')
    expected = 'hello'
    actual = testing_queue.peek()
    assert actual == expected


def test_queue_is_empty():
    testing_queue = Queue()
    expected = True
    actual = testing_queue.is_empty()
    assert actual == expected
