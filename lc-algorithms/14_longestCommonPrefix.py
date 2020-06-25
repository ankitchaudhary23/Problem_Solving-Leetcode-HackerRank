class Solution:
    def longestCommonPrefix(self, strs) -> str:
        '''
        :type str: str  
        :rtype: int
        '''
        if not strs:
            return ''
        
        str1 = min(strs)
        str2 = max(strs)
        print(str1, str2)
        for idx, char in enumerate(str1):
            print(char)
            if char != str2[idx]:
                return str1[:idx]
        return str1


def main():
    print('Given List of String: {}'.format(array))
    sol = Solution()
    result = sol.longestCommonPrefix(array)
    print('Returned Output: {}'.format(result))


if __name__ == '__main__':
    array = ["flower","flow","flight"]
    main()