# QUEUE Data Structure
# FIFO (without a head and tail)

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity #store the elements in the queue

  def append(self, item): 
    self.storage[self.current] = item
    if self.current != self.capacity - 1:
      self.current += 1
    else:
      self.current = 0

  def get(self):
    return [i for i in self.storage if i != None]