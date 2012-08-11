#!/usr/bin/python

class Heap:
    def __init__(self, A):
	self.A = A
	self.heap_size = 0
    def max_heapify(self, i):
	l = left (i)
	r = right(i)
	largest = i
	if l<length(self.A) and self.A[i]<self.A[l]:
	    largest = l
	elif r<length(self.A) and self.A[i]<self.A[r]:
	    largest = r
	if i != largest:
	    exchange(i, largest)
	    max_heap(largest)
    def build_max_heap(self):
	self.heap_size = length(A)
	int i = floor(heap_size/2)
	while i>=1:
	    max_heap(i)
	    i--
    def heap_sort(self):
	build_max_heap()
	self.heap_size = length(self.A)
	while self.heap_size >=0 :
	    max_heapify()
	    exchange(1, self.heap_size)
	    self.heap_size--
	    
    def show(self):
	"""
	print A
	"""
	print self.A

A = [12, 33, 44, 8, 90, 82, 100, 23, 38, 888, 9998]
heap = Heap(A)
heap.heap_sort()
heap.show()

