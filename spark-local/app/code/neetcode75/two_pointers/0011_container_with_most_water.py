from typing import List


class Solution:
    # region: Brute force
    """ Try every possible pair of lines.
    Let: n = number of heights
    Time Complexity: 
    - Outer loop: O(n)
    - Inner loop: O(n)
    - Overall: O(n²)
    Space Complexity: 
    - Only variables are used: O(1)
    """
    def s1_maxArea(self, height: List[int]) -> int:
        maximum = 0
        n = len(height)

        for i in range(n):
            for j in range(i+1, n):
                width = j - i
                current = width * min(height[i], height[j])
                maximum = max(maximum, current)
        return maximum
    # endregion

    # region: Optimizatin #1
    """ Two Pointer
    Let: n = number of heights
    Time Complexity: 
    - Each iteration moves exactly one pointer
    - Overall: O(n)
    Space Complexity: 
    - Only variables are used: O(1)
    """
    def s2_maxArea(self, height: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(height)-1

        while left < right:
            width = right - left
            current = width * min(height[left], height[right])
            maximum = max(maximum, current)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum
    # endregion

    # region: Optimizatin #2
    """ Two Pointer (slightly more optimized)
    Let: n = number of heights
    Time Complexity: 
    - Each iteration moves exactly one pointer
    - Overall: O(n)
    Space Complexity: 
    - Only variables are used: O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(height)-1

        while left < right:
            min_height = min(height[left], height[right])
            current = (right - left) * min_height
            maximum = max(maximum, current)
            while left < right and height[left] <= min_height:
                left += 1
            while left < right and height[right] <= min_height:
                right -= 1
        return maximum
    # endregion

def test():
    test_cases = [
        {
            "height": [1, 8, 6, 2, 5, 4, 8, 3, 7],
            "expected": 49
        },
        {
            "height": [1, 1],
            "expected": 1
        },
        {
            "height": [4, 3, 2, 1, 4],
            "expected": 16
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        result = solution.maxArea(
            tc["height"]
        )

        print(f"Test Case {i}")
        print("Input:", tc["height"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()


if __name__ == "__main__":
    test()