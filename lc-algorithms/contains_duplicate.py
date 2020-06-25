def containsDuplicate(arr):
	return len(nums) != len(set(nums))
	'''
	temp = set()
        for n in nums:
            if n in temp:
                return True
            temp.add(n)
        return False
	'''


if __name__ == '__main__':
	nums = int(input())
	arr = map(int, input().split())
	arr = list(arr)

	#print(arr)
	n = containsDuplicate(arr)
	print(n)
