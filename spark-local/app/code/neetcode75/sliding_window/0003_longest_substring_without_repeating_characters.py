class Solution:
    # region: Brute force
    """ Generate every possible substring. 
    For each substring, check whether all characters are unique.
    Let: n = length of the string
    Time Complexity: 
    - Generate substrings: O(n²)
    - Checking uniqueness ("set(substring)"): O(n)
    - Overall: O(n³)
    Space Complexity: 
    - Temporary set: O(n)
    """
    def s1_lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        for i in range(n):
            for j in range(i, n):
                substring = s[i : j+1]
                if len(substring) == len(set(substring)):
                    longest = max(longest, len(set(substring)))
        return longest
    # endregion

    # region: Optimization #1
    """ Maintain a running window using a HashSet.
    Let: n = length of the string
    Time Complexity: 
    - Each character is added once and removed once: O(2n) = O(n)
    Space Complexity: 
    - HashSet: O(n)
    """
    def s2_lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)
            
        return longest
    # endregion

    # region: Optimization #2
    """ Index HashMap
    Let: n = length of the string
    Time Complexity: 
    - Every character is processed once.: O(n)
    Space Complexity: 
    - Dictionary: O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        last_seen = {}
        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen.get(char) + 1

            last_seen[char] = right
            longest = max(longest, right - left + 1)
            
        return longest
    # endregion

def test():
    test_cases = [
        {
            "s": "abcabcbb",
            "expected": 3
        },
        {
            "s": "bbbbb",
            "expected": 1
        },
        {
            "s": "pwwkew",
            "expected": 3
        },
        {
            "s": "",
            "expected": 0
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        result = solution.lengthOfLongestSubstring(
            tc["s"]
        )

        print(f"Test Case {i}")
        print("Input:", tc["s"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()


if __name__ == "__main__":
    test()