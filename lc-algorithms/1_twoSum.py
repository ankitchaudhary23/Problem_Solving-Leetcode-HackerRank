class Solution:
	def twoSum(self, val, nums):
		'''
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		'''
		seen = {}
		for i, num in enumerate(nums):
			remaining = target - num
			if remaining in seen:
				return [seen[remaining], i]
			seen[num] = i
		return []
'''
		if len(nums)<=1:
			return false

		rng = len(nums)
		for i in range(rng):
			for j in range(i+1, rng):
				if nums[i]+nums[j] == target:
					return (i, j)
'''


def main():
	sol = Solution()
	result = sol.twoSum(target, array)
	print('Returned indicies: {}'.format(result))


if __name__ == '__main__':
	target = int(input())
	array = list(map(int, input().split()))
	main()