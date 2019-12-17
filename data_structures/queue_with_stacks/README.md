# Queues with Stacks
Challenges that utlize stacks and queues.

## Challenge Description
Create a brand new PseudoQueue class. Do not use an existing Queue. Instead,this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:

enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.
The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

## Approach & Efficiency

Big O for PseudoQueue methods:
* enqueue: O(1)
* dequeue: O(N)

## API

The PseudoQueue class has attributes stack1 and stack2. A enqueue method that adds a node to the end of the queues. A dequeue method that removes a node from the beginning of the queues.

## Solution
![whiteboard](../../assets/queue_with_stacks.jpg)
