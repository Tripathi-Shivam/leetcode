"""
This problem belongs to Arrays & Hashing because:
- Input is an array.
- We need to quickly determine whether a value has been seen before.
- A hash set provides O(1) average lookup and insertion.
- This is one of the foundational HashSet problems.
"""

from typing import List

class Solution:
    # region: solution # 1: brute force
    # Time Complexity: O(n²) 
    # Space Complexity: O(1) 
    def s1_containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        
        return False
    # endregion

    # region: solution # 2: optimization #1
    # Time Complexity: O(n log n) 
    # Space Complexity: O(1) (ignoring sorting implementation details)
    def s2_containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False    
    # endregion

    # region: solution # 3: optimization #2
    # Time Complexity: O(n) 
    # Space Complexity: O(n)
    def s3_containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False    
    # endregion

    # region: solution # 4: optimization #3
    # Time Complexity: O(n) 
    # Space Complexity: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))    
    # endregion

def test():
    test_cases = [
        {
            "nums": [1, 2, 3, 1],
            "expected": True
        },
        {
            "nums": [1, 2, 3, 4],
            "expected": False
        },
        {
            "nums": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
            "expected": True
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start = 1):
        result = solution.containsDuplicate(
            tc["nums"]
        )

        print(f"Test Case {i}")
        print("Expected", tc["expected"])
        print("Actual:", result)
        print()

if __name__ == "__main__":
    test()