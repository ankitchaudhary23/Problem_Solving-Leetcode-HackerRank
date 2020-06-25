def reverse(arr):
	result = arr.reverse()
	return result






if __name__ == '__main__':

	nums = int(input())
	arr = map(int, input().split())
	arr = list(arr)

	result = reverse(arr)
	print(result)
