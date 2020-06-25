class Solution:
    def countAndSay(self,n):
        '''
        :type str: str  
        :rtype: int
        '''
        res = '1'
        for _ in range(n-1):
            prev = res
            res = ''
            j = 0
            while j < len(prev):
                cur = prev[j]
                cnt = 1
                j +=1
                while j < len(prev) and prev[j] == cur:
                    cnt +=1
                    j+=1
                res += str(cnt) + str(cur)
        return res


def main():
    print('Given Number: {}'.format(num))
    sol = Solution()
    result = sol.countAndSay(num)
    print('Returned Output: {}'.format(result))


if __name__ == '__main__':
    num = 4
    main()