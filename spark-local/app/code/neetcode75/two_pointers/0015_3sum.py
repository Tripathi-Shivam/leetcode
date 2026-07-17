from typing import List

class Solution:
    # region: Brute force
    """ Try every possible combination of three numbers
    Let: n = number of elements
    Time Complexity: 
    - Three nested loops: O(n³)
    - Sorting each triplet: O(3 log 3)
    - Overall: O(n³)
    Space Complexity: 
    - Set stores unique triplets: O(n²) - Worst Case
    """
    def s1_threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result_set = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(
                            sorted(
                                [nums[i], nums[j], nums[k]]
                            )
                        )
                        result_set.add(triplet)
        return [list(t) for t in result_set]
    # endregion

    # region: Optimizatin #1
    """ HashSet - fix two numbers and search for the compliment
    Let: n = number of elements
    Time Complexity: 
    - Outer loop: O(n)
    - Inner loop: O(n)
    - HashSet Lookup: O(1)
    - Overall: O(n²)
    Space Complexity: 
    - HashSet: O(n) 
    - Result: O(n²)
    """
    def s2_threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result_set = set()
        for i in range(n):
            seen = set()
            for j in range(i+1, n):
                complement = - nums[i] - nums[j]
                if complement in seen:
                    triplet = tuple(
                        sorted([nums[i], nums[j], complement])
                    )
                    result_set.add(triplet)
                seen.add(nums[j])

        return [list(t) for t in result_set]
    # endregion

    # region: Optimizatin #2
    """ Sort the array, fix one number, use 2 pointers for remaining two numbers
    Let: n = number of elements
    Time Complexity: 
    - Sorting: O(n log n)
    - Outer loop: O(n)
    - Inner loop (Two pointers): O(n)
    - Overall: O(n²)
    Space Complexity (ignoring sorting implementation):
    - Result list: O(number of triplets)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return result
    # endregion

def test():
    test_cases = [
        {
            "nums": [-1, 0, 1, 2, -1, -4],
            "expected": [
                [-1, -1, 2],
                [-1, 0, 1]
            ]
        },
        {
            "nums": [0, 1, 1],
            "expected": []
        },
        {
            "nums": [0, 0, 0],
            "expected": [[0, 0, 0]]
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        result = solution.threeSum(
            tc["nums"]
        )

        print(f"Test Case {i}")
        print("Input:", tc["nums"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()


if __name__ == "__main__":
    test()