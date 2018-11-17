# below is the dynamic array implementation.
# it will let the array grow automatically when the new elements are added

import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0                              #actual count or number of elements in an array
        self.capacity = 1                       #by default it is 1 starting with first element
        self.A = self.make_array(self.capacity) #this is to create an array A(using python ctypes py_object)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        #if not 0 <= k < self.n:                    # same condition but a better way of coding
        if k < 0 or k > self.n:
            return IndexError('k is out of bound')
        return self.A[k]

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity)           #increase the capacity to two times if it is not enough
        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()


arr = DynamicArray()
arr.append(10)
print len(arr)
print arr[0]
arr.append(20)
print len(arr)


#arr.append(2)
#arr.__len__()


