#!/usr/bin/python

#Insert sort

def inserts( A ):
    i = 1
    while i < len( A ):
	if A[i] < A[i - 1]:
	    j = i - 1
	    temp = A[ i ]# A[ i ] may be changed, so don't read it again
	    while (j >= 0) and (A[j] > temp) :# this is temp not A[i];while j >= 0 ,do the next operations
		A[ j + 1 ] = A[ j ]
		j = j - 1
	    A[ j+1 ] = temp
	show_array(A)
	i = i + 1

def show_array( A ):
    for n in A:
	print n,
    print '\n'

A = [ 34, 8, -98, 3, 28, 811, 1234, 2, 4, 5, 90, 23 ]
show_array( A )
inserts( A )
show_array( A )

