# Stacks and Queues
Challenges that utlize stacks and queues.

## Challenge Description
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
Define a method called isEmpty that does not take an argument, and returns a boolean indicating whether or not the stack is empty.
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
Define a method called isEmpty that does not take an argument, and returns a boolean indicating whether or not the queue is empty.

## Approach & Efficiency
For each of the method, only one node is added/removed from the beginning of the stack or beginning/end of the queue. Hence only O(1).

Big O for Stack methods:
* push: O(1)
* pop: O(1)
* peek: O(1)
* is_empty: O(1)

Big O for Queue methods:
* enque: O(1)
* deque: O(1)
* peek: O(1)
* is_empty: O(1)


## API
The Stack class has an attribute top. A push method that adds a node to the beginning of the stacks. A pop method that removes a node from the beginning of the stacks. A peek method that returns the value of first node in the stacks. An is_empty method that returns a boolean indicating whether or not the stack is empty.

The Queue class has attributes front and end. A enqueue method that adds a node to the end of the queues. A dequeue method that removes a node from the beginning of the queues. A peek method that returns the value of first node in the queues. An is_empty method that returns a boolean indicating whether or not the queue is empty.

