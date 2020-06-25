from collections import Counter
class Solution:
    def isAnagram(self, x, y):
        '''
        :type nums: int
        :rtype: int
        '''
        # Hasmap method
        if (len(x)) != len(y):
            return False
        dic1 = {}
        dic2 = {}

        for item in x:
            dic1[item] = dic1.get(item, 0) + 1
        for item in y:
            dic2[item] = dic2.get(item, 0) + 1

        return dic1 == dic2


'''     # Sorting method
        if sorted(x) == sorted(y):
            return True
        else:
            False

'''
def main():
    print('Given array: {}, {}'.format(array1, array2))
    sol = Solution()
    result = sol.isAnagram(array1, array2)
    print('Returned Bool: {}'.format(result))


if __name__ == '__main__':
    #target = int(input())
    #array = list(map(int, input().split()))
    array1 = 'anagram'
    array2 = 'nagaram'
    main()