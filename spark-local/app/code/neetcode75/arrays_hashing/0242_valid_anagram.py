
class Solution:
    # region: solution # 1: Brute force
    # Time Complexity: O(n log n) 
    # Space Complexity: O(1) (ignoring sorting implementation details)
    def s1_isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    # endregion

    # region: solution # 2: Optimization #1
    # Time Complexity: O(n) 
    # Space Complexity: O(n)
    def s2_isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        return count_s == count_t
    # endregion

    # region: solution # 3: Optimization #2
    # Time Complexity: O(n) 
    # Space Complexity: O(n)
    def s3_isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            count[c] = count.get(c, 0) - 1
        
        for value in count.values():
            if value != 0: 
                return False
        return True
    # endregion

    # region: solution # 4: Optimization #3
    # Time Complexity: O(n) 
    # Space Complexity: O(1)
    # Note: Note: If the problem guarantees only lowercase English letters (a-z), a fixed-size array of length 26 achieves O(1) extra space.
    def s4_isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0]*26
        for c in s:
            count[ord(c) - ord("a")] += 1
        for c in t:
            count[ord(c) - ord("a")] -= 1
        
        for num in count:
            if num != 0: 
                return False
        return True
    # endregion

    # region: solution # 5: Python Alternative
    # Time Complexity: O(n) 
    # Space Complexity: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)
    # endregion

def test():

    test_cases = [
        {
            "s": "anagram",
            "t": "nagaram",
            "expected": True
        },
        {
            "s": "rat",
            "t": "car",
            "expected": False
        },
        {
            "s": "",
            "t": "",
            "expected": True
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start = 1):
        result = solution.isAnagram(tc["s"], tc["t"])

        print(f"Test Case {i}")
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()

if __name__ == "__main__":
    test()