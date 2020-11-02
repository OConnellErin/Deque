# Deque: A deque.
# Your implementation should pass the tests in test_deque.py.
# YOUR NAME

# Hint: pip3 install llist
from llist import dllist

class Deque:

    def __init__(self):
        self.data = dllist()

    def enqueue_left(self,appendee):
        self.data.appendleft(appendee)

    def enqueue_right(self,appendee):
        self.data.appendright(appendee)

    def dequeue_left(self):
        return self.data.popleft()

    def dequeue_right(self):
        return self.data.popright()        

    def is_empty(self):
        return self.data == dllist()



