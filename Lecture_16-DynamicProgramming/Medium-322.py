"""
https://leetcode.com/problems/coin-change/
"""


class Solution:
    #DP Version
    def coinChange(self, coins, amount) -> str:
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]

    def coinChangeSlow(self, coins, target):
        # Default to target value
        min_coins = target
        # Check to see if we have a single coin match (BASE CASE)
        if target in coins:
            return 1
        else:
            # for every coin value that is <= than target
            for i in [c for c in coins if c <= target]:
                # Recursive Call (add a count coin and subtract from the target)
                num_coins = 1 + self.coinChangeSlow(coins, target-i)
                # Reset Minimum if we have a new minimum
                if num_coins < min_coins:
                    min_coins = num_coins
        return min_coins

s = Solution()
print(s.coinChangeSlow([1,2,5], 11))
