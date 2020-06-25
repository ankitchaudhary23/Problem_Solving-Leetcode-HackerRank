from collections import Counter
class Solution:
    def isPalindrome(self, x):
        '''
        :type nums: int
        :rtype: int
        '''
        # Compare with Reverse 
        filtered_chars = filter(lambda ch: ch.isalnum(), x)
        lowercase_filtered_chars = map(lambda ch: ch.lower(),filtered_chars)
        filtered_chars_list = 1list(lowercase_filtered_chars)
        reverse_char_list = filtered_chars_list[::-1]
        return reverse_char_list



def main():
    print('Given array: {}'.format(array1))
    sol = Solution()
    result = sol.isPalindrome(array1)
    print('Returned Bool: {}'.format(result))


if __name__ == '__main__':
    #target = int(input())
    #array = list(map(int, input().split()))
    array1 = "A man, a plan, a canal: Panama"
    main()