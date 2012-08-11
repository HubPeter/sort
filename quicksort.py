#!/usr/bin/python

def quicksort( A, p, r ):
    if p < r:
	q = partion( A, p, r )
	quicksort( A, p, q-1 )
	quicksort( A, q+1, r )
def partion( A, p, r):
    key = A[r]
    i = p-1
    j = p
    while j < r:
	if A[j]<=key:
	    i = i + 1
	    temp = A[i]
	    A[i] = A[j]
	    A[j] = temp
	j = j + 1
    A[r] = A[i+1]
    A[i+1] = key
    return i+1


A = [1,2,3,9,332,1209,23,65,0,187,134,56,48,0,123,589,9]
quicksort(A, 0, len(A)-1 )
print A
