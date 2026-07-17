class Solution:
    # region: Brute force
    """ Repeatedly remove valid pairs
    Let: n = length of the string
    Time Complexity: 
    - Repeatedly remove valid pairs: O(n)
    - We may repeat the process roughly "n" times: O(n)
    - Overall: O(n²)
    Space Complexity: 
    - strings are immutable in Python:
    - replace() creates new strings: O(n)
    """
    def s1_isValid(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        return s == ""
    # endregion

    # region: Optimization #1
    """ Stack: What is the most recent unmatched opening bracket?
    Let: n = length of the string
    Time Complexity: 
    - We process every character once.
    - Stack operations: append → O(1) and pop → O(1)
    - For n characters: O(n)
    Space Complexity: 
    - Worst case: (((((((
    - Every character is stored in the stack: O(n)
    """
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for char in s:
            if char in mapping:
                if not stack:
                    return False
                if stack[-1] != mapping.get(char):
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
    # endregion

def test():
    test_cases = [
        {
            "s": "()",
            "expected": True
        },
        {
            "s": "()[]{}",
            "expected": True
        },
        {
            "s": "(]",
            "expected": False
        },
        {
            "s": "([])",
            "expected": True
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        result = solution.isValid(
            tc["s"]
        )

        print(f"Test Case {i}")
        print("Input:", tc["s"])
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()


if __name__ == "__main__":
    test()