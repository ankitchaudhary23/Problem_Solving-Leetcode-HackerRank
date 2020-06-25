class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        :type str: str  
        :rtype: int
        '''
        if len(needle) == '':
            return 0

        stackLen = len(haystack)
        needLen = len(needle)

        for i in range(stackLen-needLen+1):
            for j in range(needLen):
                if haystack[i] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1


def main():
    print('Given String: {}'.format(array1))
    sol = Solution()
    result = sol.strStr(array1, array2)
    print('Returned Output: {}'.format(result))


if __name__ == '__main__':
    #target = int(input())
    #array = list(map(int, input().split()))
    array1 = 'hello'
    array2 = 'll'
    main()