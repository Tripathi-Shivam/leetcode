from typing import List


class Solution:
    # region: Brute force
    """ Scan every number and track the minimum
    Let: n = length of nums
    Time Complexity: 
    - Overall: O(n)
    Space Complexity: 
    - Overall: O(1)
    """
    def s1_findMin(self, nums: List[int]) -> int:
        minimum = float("infinity")
        for num in nums:
            minimum = min(minimum, num)
        return minimum
    # endregion

    # region: Optimization #1
    """ Binary Search
    Let: n = length of nums
    Time Complexity: 
    - Overall: log₂(n)
    Space Complexity: 
    - Overall: O(1)
    """
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= nums[right]:
                left = mid + 1
            else: 
                right = mid
        return nums[left]
    # endregion

def test():
    test_cases = [
        {
            "nums": [3, 4, 5, 1, 2],
            "expected": 1
        },
        {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "expected": 0
        },
        {
            "nums": [11, 13, 15, 17],
            "expected": 11
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        result = solution.findMin(
            tc["nums"]
        )

        print(f"Test Case {i}")
        print("Input:", tc["nums"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()


if __name__ == "__main__":
    test()