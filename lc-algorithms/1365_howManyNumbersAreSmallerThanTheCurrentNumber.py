class Solution():
	def smallerNumbersThanCurrent(self, nums):
		'''
		type: list[]
		rtype: lsit[]
		'''
		dic = {}
		sortedList = sorted(nums)
		for i, num in enumerate(nums):
			if num not in dic:
				dic[num] = i
		return [dic[num] for num in nums]

'''	# brute force	
		temp = []
		arrlen = len(nums)

		for i in range(arrlen):
			cnt = 0
			for j in range(arrlen):
				if nums[i] > nums[j]:
					cnt += 1
			temp.append(cnt)
		return temp
'''


def main():
	print('Given Array: {}'.format(array))

	sol = Solution()
	result = sol.smallerNumbersThanCurrent(array)

	print('Returned Array: {}'.format(result))



if __name__ == '__main__':
	array = list(map(int, input().split()))
	main()