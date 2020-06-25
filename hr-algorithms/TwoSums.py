nums = [2,15,11,7]
target = 9

def twoSum(nums, target):
#	for i in range(len(nums) -1):
#		for j  in range(i+1, len(nums)):
#			if nums[i] + nums[j] == target:
#				return (i, j)

#print(twoSum(nums, target))


	h = {}
	
	for i, num in enumerate(nums):
		n = target - num
		#print(i, n, num)
		if n not in h:
			print(n, num, h)
			h[num] = i
			print (h[num])
			#print(h)
		else:
			print (h[n], i)
			#return(h[n],i)
			


print(twoSum(nums, target))






