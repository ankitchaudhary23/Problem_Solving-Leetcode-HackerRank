class Solution:
	def intersetcion(self, set1, set2):
		set1 = set(array1)
		set2 = set(array2)
		return set1, set2




def main():
	print('Array 1 :'.format(array1))
	print('Array 2 :'.format(array2))

	sol = Solution()
	result = sol.intersetcion(array1, array2)

	print('Set1 is '.format(set1))
	print('Set2 is '.format(set2))



if __name__ == '__main__':
	array1 = list(map(int, input().split()))
	array2 = list(map(int, input().split()))

	main()