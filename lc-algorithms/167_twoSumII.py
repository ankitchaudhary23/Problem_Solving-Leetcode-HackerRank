class Solution:
	def twoSumII(self, val, nums):
		'''
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		'''
		# dictionary
		dic = {}
		for i, num in enumerate(nums):
			if target - num in dic:
				return [dic[target-num]+1, i+1]
			dic[num] = i
''' # two pointers
		first, last = 0, len(nums) -1
		while last > first:
			sum = nums[first]+nums[last]
			if sum > target:
				last-=1
			elif sum == target:
				return (first+1, last +1)
			else:
				first+=1
'''


def main():
	sol = Solution()
	result = sol.twoSumII(target, array)
	print('Returned indicies: {}'.format(result))


if __name__ == '__main__':
	#target = int(input())
	#array = list(map(int, input().split()))
	target = 9
	array = [2,7,11,15]
	main()