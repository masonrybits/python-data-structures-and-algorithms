from data_structures.stacks_and_queues.stacks_and_queues import Node, Stack, EmptyQueueException
from queue_with_stacks import PseudoQueue
import pytest

def test_pseudoqueue_dequeue_multiple():
    testing_queue = PseudoQueue(Stack())
    testing_queue.enqueue(1)
    testing_queue.enqueue(2)
    testing_queue.dequeue()
    expected = 2
    actual = testing_queue.peek()
    assert actual == expected

def test_pseudoqueue_enqueue_multiple():
    testing_queue = PseudoQueue(Stack())
    testing_queue.enqueue(1)
    testing_queue.enqueue(2)
    testing_queue.enqueue(3)
    expected = 3
    actual = testing_queue.peek()
    assert actual == expected

def test_stack_empty_dequeue():
    testing_queue = PseudoQueue(Stack())
    with pytest.raises(EmptyQueueException):
        assert testing_queue.dequeue()
