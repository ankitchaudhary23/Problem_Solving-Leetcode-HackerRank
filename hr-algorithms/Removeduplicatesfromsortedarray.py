def removeDuplicates(arr):

	#if n <= 1:
	#	return n

	j = 0

	for i in range(len(arr) -1):
		if arr[i] != arr[i+1]:
			print(arr[i])
			arr[j] = arr[i]
			j += 1

	arr[j] = arr[-1]
	j +=1
	return j


arr = [1,2,2,3,4,4,4,5,5,5]
#n = len(arr)
n = []
# new size of array
n = removeDuplicates(arr)

# Print updated array 
for i in range(0, n): 
	print (" %d " %(arr[i]), end = " ") 