from typing import List


class Solution:
    # region: Brute force
    """ Try every possible buy day. For each buy day, try every possible sell day.
    Let: n = number of days
    Time Complexity: 
    - Outer loop: O(n)
    - Inner loop: O(n)
    - Overall: O(n²)
    Space Complexity: 
    - Only variables are used: O(1)
    """
    def s1_maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        n = len(prices)
        for buy in range(n):
            for sell in range(buy+1, n):
                profit = prices[sell] - prices[buy]
                maximum = max(maximum, profit)
        return maximum
    # endregion

    # region: Optimization #1
    """ Running Minimum
    Let: n = number of days
    Time Complexity: 
    - Each price is visited exactly once: O(n)
    Space Complexity: 
    - Only variables are used: O(1)
    """
    def s2_maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0

        for prices in prices[1:]:
            minimum = min(minimum, prices)
            max_profit = max(max_profit, prices - minimum)
            
        return max_profit
    # endregion

    # region: Optimization #2
    """ Optimal Sliding Window
    Let: n = number of days
    Time Complexity: 
    - Both pointers move only forward.
    - Each index is visited at most once: O(n)
    Space Complexity: 
    - Only variables are used: O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1            

        return max_profit
    # endregion

def test():

    test_cases = [
        {
            "prices": [7, 1, 5, 3, 6, 4],
            "expected": 5
        },
        {
            "prices": [7, 6, 4, 3, 1],
            "expected": 0
        },
        {
            "prices": [2, 4, 1],
            "expected": 2
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        result = solution.maxProfit(
            tc["prices"]
        )

        print(f"Test Case {i}")
        print("Input:", tc["prices"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()


if __name__ == "__main__":
    test()