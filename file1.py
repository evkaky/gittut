from itertools import count

arr = [1, 2, 3, 4, 5]


class MyRange:
   def __init__(self):
      self.arr = []
      self.idx = 0

   def __iter__(self):
      return self

   def __next__(self):
      try:
         res = self.arr[self.idx]
      except IndexError:
         raise StopIteration
      self.idx += 1
      return res



def my_chain(*iterables):
   for it in iterables:
      yield from it

def my_enumerate(iterable, start=0):
   i = start
   for item in iterable:
      yield (i, item)
      i += 1

def my_enumerate2(iterable, start=0):
   return zip(iterable, count(start))


for i, item in my_enumerate([1,2,3]):
   print(i, item)


