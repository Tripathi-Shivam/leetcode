from collections import Counter


class Solution:
    # region: Brute force #1
    """ Generate every substring.
    For each substring: 
    - Count characters.
    - Check if every character of t exists with sufficient frequency.
    Let: n = len(s), m = len(t)
    Time Complexity: 
    - Generate substrings: O(n²)
    - Counting frequencies:: O(n)
    - Overall: O(n³)
    Space Complexity: 
    - Counter: O(m)
    """
    def s1_minWindow(self, s: str, t: str) -> str:
        countT = {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        answer = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                window = s[i:j+1]
                windowCount = {}
                for char in window:
                    windowCount[char] = windowCount.get(char, 0) + 1
                valid = True
                for char in countT:
                    if char not in windowCount or windowCount[char] < countT[char]:
                        valid = False
                        break
                if valid and (answer == "" or len(window) < len(answer)):
                    answer = window
        return answer
    # endregion

    # region: Brute force #2
    """ Generate every substring.
    For each substring: 
    - Count characters.
    - Check if every character of t exists with sufficient frequency.
    Let: n = len(s), m = len(t)
    Time Complexity: 
    - Overall: O(n² * m)
    Space Complexity: 
    - Counter: O(m)
    """
    def s2_minWindow(self, s: str, t: str) -> str:
        countT = {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        res, resLen = [-1, -1], float("infinity")
        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                countS[s[j]] = countS.get(s[j], 0) + 1
                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break
                if flag and (j - i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
    # endregion

    # region: Optimization #1
    """ Maintain counts while sliding.
    Let: n = len(s), m = total number of unique characters in the strings t and s
    Time Complexity: 
    - Overall: O(n+m)
    Space Complexity: 
    - Counter: O(m)
    """
    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ""

        countT, window = {}, {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        have, need = 0, len(countT)
        left = 0
        result, result_len = [-1, -1], float("infinity")
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < result_len:
                    result_len = (right - left + 1)
                    result = [left, right]

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1
        left, right = result
        return s[left : right + 1] if result_len != float("infinity") else ""
    # endregion


def test():

    test_cases = [
        {
            "s": "ADOBECODEBANC",
            "t": "ABC",
            "expected": "BANC"
        },
        {
            "s": "a",
            "t": "a",
            "expected": "a"
        },
        {
            "s": "a",
            "t": "aa",
            "expected": ""
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        result = solution.minWindow(
            tc["s"],
            tc["t"]
        )

        print(f"Test Case {i}")
        print("Input: s =", tc["s"])
        print("Input: t =", tc["t"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()


if __name__ == "__main__":
    test()