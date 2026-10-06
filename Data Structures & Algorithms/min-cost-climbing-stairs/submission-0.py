class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] is the cost of taking a step from the ith floor of a staircase. 
        #  paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
        a, b = 0, 0
        for i in range(2, len(cost) + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b