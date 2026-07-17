from typing import List

class Solution:
    # region: Brute force
    """ For every index, multiply every other element
    Let: n = number of elements
    Time Complexity: 
    - Outer loop: O(n)
    - Inner loop: O(n)
    - Overall: O(n²)
    Space Complexity: 
    - Result array: O(n)
    - Extra variables: O(1)
    - Overall (excluding required output): O(1)
    - If counting the output array: O(n)
    """
    def s1_productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            result.append(product)
        return result
    # endregion

    # region: Optimization #1
    """ Precompute: Prefix products & Suffix products
    Let: n = number of elements
    Time Complexity: 
    - Build prefix: O(n)
    - Build suffix: O(n)
    - Build result: O(n)
    - Overall: O(n)
    Space Complexity: 
    - Prefix: O(n)
    - Suffix: O(n)
    - Result: O(n)
    - Extra space (excluding output): O(n)
    """
    def s2_productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        result = [1]*n
        for i in range(n):
            result[i] = prefix[i]*suffix[i]

        return result
    # endregion

    # region: Optimization #2
    """ Notice we don't need a separate prefix array
    Let: n = number of elements
    Time Complexity: 
    - First pass (prefix): O(n)
    - Second pass (suffix): O(n)
    - Overall: O(n)
    Space Complexity: 
    - Result: O(n)
    - Extra space (excluding output): O(1)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
    # endregion

def test():
    test_cases = [
        {
            "nums": [1,2,3,4],
            "expected": [24,12,8,6]
        },
        {
            "nums": [-1,1,0,-3,3],
            "expected": [0,0,9,0,0]
        },
        {
            "nums": [10,20],
            "expected": [20,10]
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):
        result = solution.productExceptSelf(tc["nums"])

        print(f"Test Case {i}")
        print("Input:", tc["nums"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()

if __name__ == "__main__":
    test()