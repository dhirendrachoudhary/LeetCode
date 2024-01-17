class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for wealth in accounts:
            if richest < sum(wealth):
                richest = sum(wealth)
        return richest
        