from typing import List

class Solution:
    # region: solution # 1: Brute force
    # Time Complexity: O(n²)
    # Space Complexity: O(1)
    def s1_twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]
    # endregion

    # region: solution # 2: Optimization #1
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def s2_twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = sorted(
            enumerate(nums),
            key = lambda x: x[1]
        )
        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = indexed_nums[left][1] + indexed_nums[right][1]
            if current_sum == target:
                return [indexed_nums[left][0], indexed_nums[right][0]]
            elif current_sum < target:
                left +=1
            else:
                right -= 1

        return [-1, -1]
    # endregion

    # region: solution # 3: Optimization #2
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        return [-1, -1]
    # endregion


def test():
    test_cases = [
        {
            "nums": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1]
        },
        {
            "nums": [3, 2, 4],
            "target": 6,
            "expected": [1, 2]
        },
        {
            "nums": [3, 3],
            "target": 6,
            "expected": [0, 1]
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start = 1):
        result = solution.twoSum(tc["nums"], tc["target"])

        print(f"Test Case {i}")
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()

if __name__ == "__main__":
    test()