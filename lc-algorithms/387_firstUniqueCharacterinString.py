from collections import Counter
class Solution:
	def firstUniqChar(self, x):
		'''
		:type nums: int
		:rtype: int
		'''
		# build hash map
		count = collections.Counter(x)
		for idx, char in enumerate(x):
			if count[char] == 1:
				return idx
		return -1


def main():
	print('Given array: {}'.format(array))
	sol = Solution()
	result = sol.firstUniqChar(array)
	print('Returned Index: {}'.format(result))


if __name__ == '__main__':
	#target = int(input())
	#array = list(map(int, input().split()))
	array = 'leetcode'
	main()