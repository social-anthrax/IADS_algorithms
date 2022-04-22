#!/usr/bin/python

A = [5, 23, 3, 14, 2]

def merge(B, C):
	i = j = 0
	res = []
#	for k in range (0,len(B)+len()):
	while i<len(B) and j<len(C):
		if B[i] < C[j]:
			res.append(B[i])
			i += 1
		else:
			res.append(C[j])
			j += 1
	res += B[i:]
	res += C[j:]
	return res

def mergeSort(A):
	
	if len(A) <= 1:
		return A
	mid = len(A)//2
	print("Split into:",A[:mid],A[mid:])
	B = mergeSort (A[:mid])
	C = mergeSort (A[mid:])
	D = merge(B, C)
	print("After merge:",D)
	return D

mergeSort(A)