"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return "Cannot pop: Stack is empty."
        return self.items.pop()


    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue = deque()


    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.queue.append(value)
        #Items added to back wait in line until the front items are removed.
    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return "Cannot dequeue: Queue is empty."
        return self.queue.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return "Cannot view front: Queue is empty."
        return self.queue[0]
        #returns item at front of queue or index 0.


    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.queue) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO Testing Stack (LIFO) ===")
my_stack = Stack()
my_stack.push("Ubuntu")
my_stack.push("Debian")
my_stack.push("Pop!_OS")
my_stack.push("Alpine Linux")
print("Pushed 4 Linux distributions to the stack.")

print(f"Popping the top item: {my_stack.pop()}")
print(f"Peeking at the new top item: {my_stack.peek()}")

print("\n--- Testing Stack Edge Cases ---")
empty_stack = Stack()
print(f"Popping from empty stack: {empty_stack.pop()}")
print(f"Peeking at empty stack: {empty_stack.peek()}")

single_item_stack = Stack()
single_item_stack.push("Only item")
single_item_stack.pop()
print(f"Is single-item stack empty after removal?: {single_item_stack.is_empty()}")

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
my_queue = Queue()
my_queue.enqueue("Rick and Morty")
my_queue.enqueue("Solar Opposites")
my_queue.enqueue("The Crown")
my_queue.enqueue("Dexter: Resurrection")
print("Enqueued 4 TV shows.")

print(f"Dequeuing the front item: {my_queue.dequeue()}")
print(f"Viewing the new front item: {my_queue.front()}")

print("\n--- Testing Queue Edge Cases ---")
empty_queue = Queue()
print(f"Dequeuing from empty queue: {empty_queue.dequeue()}")
print(f"Viewing front of empty queue: {empty_queue.front()}")

single_item_queue = Queue()
single_item_queue.enqueue("Only Item")
single_item_queue.dequeue()
print(f"Is single-item queue empty after removal?: {single_item_queue.is_empty()}")

if __name__ == "__main__":
    main()
