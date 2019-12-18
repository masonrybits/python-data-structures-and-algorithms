from fifo_animal_shelter import AnimalShelter, Cat, Dog
from data_structures.stacks_and_queues.stacks_and_queues import Stack, EmptyStackException
import pytest

def test_AnimalShelter_enqueue_multiple():
    animal_queue = AnimalShelter()
    animal_queue.enqueue(Cat())
    animal_queue.enqueue(Cat())
    animal_queue.enqueue(Dog())
    expected = Cat()
    actual = animal_queue.peek()
    assert actual == expected

def test_queue_empty_dequeue():
    animal_queue = AnimalShelter()
    with pytest.raises(EmptyStackException):
        assert animal_queue.dequeue(Cat())
