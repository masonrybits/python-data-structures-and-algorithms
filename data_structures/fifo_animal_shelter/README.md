# Queues with Stacks
Challenges that utlize stacks and queues.

## Challenge Description
Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

## Approach & Efficiency

Big O of space for AnimalShelter methods:
* enqueue: O(1)
* dequeue: O(1)

Big O of time for AnimalShelter methods:
* enqueue: O(N)
* dequeue: O(N)

## API

The PseudoQueue class has attributes stamain_stackck and helper_stack. A enqueue method that adds a node to the end of the queues. A dequeue method that removes a node from the beginning of the queues.

## Solution
![whiteboard](../../assets/fifo_animal_shelter.jpg)
