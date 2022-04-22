"""
Step by step inplace insertion sort 
1. Find a pivot x
2. Traverse all values before x, if it is larger than x, move to the right
3. Stop if one value is not larger than x, or all values before x are evaluated
4. j+1 is where x supposed to be after that round of sorting. 
"""
A = [5, 23, 3, 14, 2]

def insertSort(L):
	n = len(L)
	for i in range (1,n):
		x = L[i]
		j = i-1
		while j >= 0 and L[j] > x:
			L[j+1] = L[j] 
			j -= 1
		L[j+1] = x
		print("When i =",i)
		print(L)
		
insertSort(A)