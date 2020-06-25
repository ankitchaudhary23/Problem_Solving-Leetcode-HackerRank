import re
class Solution:
    def myAtoi(self, str: str) -> int:
        '''
        :type str: str  
        :rtype: int
        '''
        str = str.strip()
        str = re.findall('^[+\-]?\d+' ,str)

        try:
        	res = int(''.join(str))
        	max = 2147483647
        	min = -2147483648
        	if res>max:
        		return max
        	elif res<min:
        		return min
        	else:
        		return res
        except:
        	return 0



def main():
    print('Given String: {}'.format(array1))
    sol = Solution()
    result = sol.myAtoi(array1)
    print('Returned Atoi Value: {}'.format(result))


if __name__ == '__main__':
    #target = int(input())
    #array = list(map(int, input().split()))
    array1 = ' -42'
    main()