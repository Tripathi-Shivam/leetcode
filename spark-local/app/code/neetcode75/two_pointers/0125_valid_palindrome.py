class Solution:
    # region: Brute force
    """ Build a cleaned string. Reverse it. Compare both strings.
    Let: n = length of the original string
    Time Complexity: 
    - Building cleaned string: O(n)
    - Reversing: O(n)
    - Comparing: O(n)
    - Overall: O(n)
    Space Complexity: 
    - Cleaned string: O(n)
    - Reversed string: O(n)
    - Overall: O(n)
    """
    def s1_isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        return cleaned == cleaned[::-1]
    # endregion

    # region: Optimization #1
    """ Use two pointers. Skip invalid characters. Compare characters directly.
    Let: n = length of the original string
    Time Complexity: 
    - Each pointer moves across the string at most once: O(n)
    Space Complexity: 
    - Only two pointers: O(1)
    """
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True

    # endregion

def test():

    test_cases = [
        {
            "s": "A man, a plan, a canal: Panama",
            "expected": True
        },
        {
            "s": "race a car",
            "expected": False
        },
        {
            "s": " ",
            "expected": True
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        result = solution.isPalindrome(
            tc["s"]
        )

        print(f"Test Case {i}")
        print("Input:", tc["s"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()


if __name__ == "__main__":
    test()