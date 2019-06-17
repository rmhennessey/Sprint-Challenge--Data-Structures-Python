# remove duplicate names found between the 2 lists
# find a faster way to to do this.
# 1) Binary Search Tree

    # 2) SET
    # also discovered set() in python: https://stackoverflow.com/questions/1675321/fastest-way-to-remove-duplicates-in-lists-python
    # a set cannot contain duplicate entries


import time


#literally the code from the earlier week's project.
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # check if the new node's value is less than our current node's value
    if value < self.value:
      # if there's no left child here already, place the new node here
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        # otherwise, repeat the process!
        self.left.insert(value)
    # check if the new node's value is greater than or equal to our current node's value
    elif value >= self.value:
      # if there's no right child here already, place the new node here
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        # otherwise, repeat the process!
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    
    elif target < self.value:
      if not self.left:
      # can also do if self.left == None: 
        return False
      else:
        return self.left.contains(target)
  
    # else: target > self.value:
    else:
      if not self.right:
      # if self.right == None:
        return False
      return self.right.contains(target)

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# *** OG ***
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1) # runtime 5.7 seconds


# *** BST ***
# duplicates = []
# bst = BinarySearchTree(names_1.pop())
# for name_1 in names_1:
#     bst.insert(name_1)

# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2) #runtime 0.10


# *** SET ***
    # sets vs lists in terms of speed: https://stackoverflow.com/questions/2831212/python-sets-vs-lists
    # tl;dr Lists are slightly faster than sets when you just want to iterate over the values.
    # Sets, however, are significantly faster than lists if you want to check if an item is contained within it. 
    # Sets can only contain unique items though.

# names_1 = list(set(names_1)) #runtime of 1.46 seconds

names_1 = set(names_1) # runtime of 0.0072 seconds

duplicates = []
for name in names_2:
    if name in names_1:
        duplicates.append(name) # runtime 0.006


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

