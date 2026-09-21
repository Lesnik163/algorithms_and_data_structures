def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n-1)

def recursive_sum(arr):
  if len(arr) == 0:
    return 0
  else:
    return arr[0] + recursive_sum(arr[1:])


def recursive_binary_search(arr, low, high, target):
  if low > high:
    return -1
  mid = (low + high) // 2
  if arr[mid] == target:
    return mid
  if arr[mid] < target:
    return recursive_binary_search(arr, mid + 1, high, target)
  return recursive_binary_search(arr, low, mid - 1, target)

class Stack:
  def __init__(self):
    self.items = []
  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def is_empty(self):
    return len(self.items) == 0
  def size(self):
    return len(self.items)
  def peek(self):
    return self.items[-1]