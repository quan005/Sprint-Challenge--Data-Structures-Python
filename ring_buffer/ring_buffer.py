from queue import Queue

# My Notes:
# Im using a list as my buffer storage because its easy to append items and it has mutability
# to easily mutate the oldest item.
# I need to Keep track of the oldest item and newest item
# I need to keep track of the length of the list
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.storage = []
        self.old = -1 # The last item in the list is the oldest item until the list reaches capacity
        self.new = 0 # The first item in the list 

    def append(self, item):
        # If the length of my list is less than the capacity, then i can simply add
        # the item to the list.
        if self.length < self.capacity:
            self.storage.append(item)
            self.length += 1
        # If the list is at capacity then we need to figure out whats the oldest item
        # and change it
        else:
            print('old', self.old)
            print('old plus one', self.old + 1)
            print('new old', (self.old + 1) % self.capacity)
            self.old = (self.old + 1) % self.capacity
            self.storage[self.old] = item
            self.length += 1

    def get(self):
        if self.length == 0:
            return 'ring buffer is empty'
        return self.storage