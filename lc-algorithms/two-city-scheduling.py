class solution:
	def twoCitySchedCity(self, costs):
		sorted_cost = sorted(costs, key = lambda x:x[0]-x[1])

		total_cost  = 0
		n = len(costs)//2

		for i in range(n):
			total_cost += sorted_cost[i][0] + sorted_cost[i+n][1]
		return total_cost


costs = [[10,20], [30,200], [400,50], [30,20]]

sol = solution()
print(sol.twoCitySchedCity(costs))