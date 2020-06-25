
class Solution:
    def removeDuplicates(self,nums):
        if len(nums) <=1:
            return 0
        
        j = 0
        
        for i in range(len(nums[0:-1])):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        
        nums[j] = nums[-1]
        j +=1
        return j
        


def main():
    print('Array is : {}'.format(array))

    sol = Solution()
    res = sol.removeDuplicates(array)

    #print('Removed Duplicates : {}'.format(res))
    print('Length of New Array : {}'.format(res))


if __name__ == '__main__':
    arr_count = int(input())
    array = list(map(str, input().split()))

    main()