def singleNumber(nums):
	
	# 1st method
    #return 2*sum(set(nums)) - sum(nums)

    # 2nd method
    ans = set()
    for num in nums:
    	if num in ans:
    		ans.remove(num)
    	else:
    		ans.add(num)

    return ans.pop()

    # 3rd method
    res = 0
    for num in nums:
    	res ^= num
    return res


if __name__ == '__main__':

	#nums = [int(input()) for _ in range(int(input()))]
	#print(nums)
	'''
	that's how we get array through terminal
	'''
	nums = int(input())
	arr = map(int, input().split())
	arr = list(arr)

	#print(set(arr))
	#print(sum(set(arr)))
	#print(sum(arr))

	n = singleNumber(arr)
	print(n)