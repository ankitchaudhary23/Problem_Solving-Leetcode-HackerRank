class Solution:
	def maxProfit(self, prices):
		# @param: prices, an integer
		# @return: an integer
		if len(prices) <= 1:
			return 0

		profit = 0
		for i in range(1, len(prices)):
			if prices[i] > prices[i-1]:
				profit += prices[i] - prices[i-1]
		return profit



def main():
	print('Stock Prices : {}'.format(prices))
	sol = Solution()
	res = sol.maxProfit(prices)
	print('Maximum Profit earned : {}'.format(res))


if __name__ == '__main__':
	arrCount = int(input())
	prices = list(map(int, input().split()))

	main()
