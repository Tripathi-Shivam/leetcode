from typing import List


class Solution:
    # region: Brute force
    """ Scan the array and return the target's index
    Let: n = length of nums
    Time Complexity: 
    - Overall: O(n)
    Space Complexity: 
    - Overall: O(1)
    """
    def s1_search(self, nums: List[int], target: int) -> int:
        for index, num in enumerate(nums):
            if num == target:
                return index
        return -1
    # endregion

    # region: Optimization #1
    """ Binary Search
    Let: n = length of nums
    Time Complexity: 
    - Overall: log₂(n)
    Space Complexity: 
    - Overall: O(1)
    """
    def s2_search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)
    # endregion

    # region: Optimization #2
    """ Binary Search (Two Pass)
    Let: n = length of nums
    Time Complexity: 
    - Overall: log₂(n)
    Space Complexity: 
    - Overall: O(1)
    """
    def s2_search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        l, r = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
    # endregion

    # region: Optimization #3
    """ Binary Search (One Pass)
    Let: n = length of nums
    Time Complexity: 
    - Overall: log₂(n)
    Space Complexity: 
    - Overall: O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
    # endregion


def test():

    test_cases = [
        {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 0,
            "expected": 4
        },
        {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 3,
            "expected": -1
        },
        {
            "nums": [1],
            "target": 0,
            "expected": -1
        },
        {
            "nums": [1,3],
            "target": 3,
            "expected": 1
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        result = solution.search(
            tc["nums"],
            tc["target"]
        )

        print(f"Test Case {i}")
        print("Input:", tc["nums"], "Target:", tc["target"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()


if __name__ == "__main__":
    test()