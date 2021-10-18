from typing import List
from sys import maxsize


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = max_price_so_far = prices[0]
        max_profit_so_far = 0

        for price in prices:
            if price < min_price_so_far:
                min_price_so_far = price
                # Reset the max price to same index value since it should be on or after min price
                max_price_so_far = price
                continue

            if price > max_price_so_far:
                max_price_so_far = price

            max_profit_so_far = max(max_price_so_far - min_price_so_far, max_profit_so_far)

        return max_profit_so_far


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit(prices=[7, 6, 4, 3, 1]))
