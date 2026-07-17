from typing import List

class Solution:
    # region: Brute force
    """ For every number: Keep checking whether the next consecutive number exists.
    Let: n = number of elements
    Time Complexity: 
    - Outer loop: O(n)
    - Membership check: O(n)
    - Overall: O(n²)
    Space Complexity: 
    - Only variables: O(1)
    """
    def s1_longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 0
        for num in nums:
            current = num
            length = 1
            while current + 1 in nums:
                current += 1
                length += 1
            
            longest = max(longest, length)

        return longest
    # endregion

    # region: Optimization #1
    """ Sorting
    Let: n = number of elements
    Time Complexity: 
    - Sorting: O(n log n)
    - Scan: O(n)
    - Overall: O(n log n)
    Space Complexity: 
    - Ignoring sorting implementation: O(1)
    """
    def s2_longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()        
        longest = current = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)
    # endregion

    # region: Optimization #2
    """ HashSet - Only begin counting if: "num-1" does not exist
    Let: n = number of elements
    Time Complexity: 
    - Building the set: O(n)
    - Outer loop: O(n)
    - Inner loop looks expensive but each number is visited only once.
    - Total inner loop work: O(n)
    - Overall: O(n)
    Space Complexity: 
    - HashSet: O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        longest = 1
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 1
                while current+1 in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
    # endregion

def test():
    test_cases = [
        {
            "nums": [100,4,200,1,3,2],
            "expected": 4
        },
        {
            "nums": [0,3,7,2,5,8,4,6,0,1],
            "expected": 9
        },
        {
            "nums": [1,0,1,2],
            "expected": 3
        }
    ]
    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):
        result = solution.longestConsecutive(
            tc["nums"]
        )

        print(f"Test Case {i}")
        print("Input:", tc["nums"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()

if __name__ == "__main__":
    test()