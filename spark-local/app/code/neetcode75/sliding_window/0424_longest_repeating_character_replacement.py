class Solution:
    # region: Brute force
    """ Generate every substring.
    For each substring: 
    - Count character frequencies.
    - Find the most frequent character.
    - Compute how many replacements are needed.
    Let: n = length of the string
    Time Complexity: 
    - Generate substrings: O(n²)
    - Counting frequencies:: O(n)
    - Overall: O(n³)
    Space Complexity: 
    - Counter: O(n)
    """
    def s1_characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        n = len(s)
        longest = 0
        for i in range(n):
            for j in range(i, n):
                substring = s[i : j+1]
                counter = Counter(substring)
                max_freq = max(counter.values())
                replacements = len(substring) - max_freq
                if replacements <= k:
                    longest = max(longest, len(substring))
        return longest
    # endregion

    # region: Brute force #2
    """ Generate every substring.
    For each substring: 
    - Count character frequencies.
    - Find the most frequent character.
    - Compute how many replacements are needed.
    Let: n = length of the string, m = total number of unique characters
    Time Complexity: 
    - Overall: O(n²)
    Space Complexity: 
    - Counter: O(m)
    """
    def s2_characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        longest = 0
        for i in range(n):
            count, max_freq = {}, 0
            for j in range(i, n):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(max_freq, count[s[j]])
                window = j - i + 1
                replacements = window - max_freq
                if replacements <= k:
                    longest = max(longest, window)
        return longest
    # endregion

    # region: Optimization #1
    """ Maintain frequencies while sliding the window.
    Instead of recomputing counts every time.
    Let: n = length of the string, m = total number of unique characters
    Time Complexity: 
    - Overall: O(n)
    Space Complexity: 
    - Counter: O(m)
    """
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        longest = 0
        max_freq = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            # while (right - left + 1) - max(count.values()) > k: # O(26)
            while (right - left + 1) - max_freq > k: # O(1): result will only update max_freq increases
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
    # endregion

def test():
    test_cases = [
        {
            "s": "ABAB",
            "k": 2,
            "expected": 4
        },
        {
            "s": "AABABBA",
            "k": 1,
            "expected": 4
        },
        {
            "s": "AAAA",
            "k": 2,
            "expected": 4
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        result = solution.characterReplacement(
            tc["s"],
            tc["k"]
        )

        print(f"Test Case {i}")
        print("Input:", tc["s"], tc["k"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()


if __name__ == "__main__":
    test()