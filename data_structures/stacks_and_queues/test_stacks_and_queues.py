from stacks_and_queues import Node, Stack, Queue, EmptyStackException, EmptyQueueException

import pytest


def test_stack_push():
    testing_stack = Stack()
    testing_stack.push(2)
    expected = 2
    actual = testing_stack.peek()
    assert actual == expected


def test_stack_push_multiple():
    testing_stack = Stack()
    testing_stack.push(1)
    testing_stack.push(2)
    testing_stack.push(3)
    expected = 3
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


def test_stack_empty_pop():
    testing_stack = Stack()
    with pytest.raises(EmptyStackException):
        assert testing_stack.pop()


def test_queue_enqueue():
    testing_queue = Queue()
    testing_queue.enqueue(1)
    testing_queue.enqueue(2)
    expected = 1
    actual = testing_queue.peek()
    assert actual == expected


def test_queue_enqueue_multiple():
    testing_queue = Queue()
    testing_queue.enqueue(1)
    testing_queue.enqueue(2)
    testing_queue.enqueue(3)
    expected = 1
    actual = testing_queue.peek()
    assert actual == expected


def test_queue_dequeue():
    testing_queue = Queue()
    testing_queue.enqueue(1)
    testing_queue.enqueue(2)
    testing_queue.dequeue()
    expected = 2
    actual = testing_queue.peek()
    assert actual == expected


def test_queue_peek():
    testing_queue = Queue()
    testing_queue.enqueue('hello')
    testing_queue.enqueue('hallo')
    expected = 'hello'
    actual = testing_queue.peek()
    assert actual == expected


def test_queue_is_empty():
    testing_queue = Queue()
    expected = True
    actual = testing_queue.is_empty()
    assert actual == expected


def test_queue_empty_dequeue():
    testing_queue = Queue()
    with pytest.raises(EmptyQueueException):
        assert testing_queue.dequeue()
