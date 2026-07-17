from collections import defaultdict
from typing import List

class Solution:
    # region: solution # 1.1: Brute force
    """ Sorting
    Let: n = number of strings & k = average string length
    Time Complexity: 
    - Overall: O(n² * k log k)
    Space Complexity: 
    - Overall: O(n)
    """
    def s1_1_groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = [False]*len(strs)
        result = []
        for i in range(len(strs)):
            if visited[i]:
                continue
            group = [strs[i]]
            visited[i] = True
            for j in range(i+1, len(strs)):
                if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    visited[j] = True
            result.append(group)
        return result
    # endregion
    
    # region: solution # 1.2: Brute force
    # Time Complexity: O(n²)
    # Space Complexity: O(n)
    def s1_2_groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        visited = [False] * n
        result = []

        for i in range(n):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            count_i = [0]*26
            for s in strs[i]:
                count_i[ord(s) - ord("a")] += 1

            for j in range(i+1, n):
                if visited[j] == False:
                    count_j = [0]*26
                    for s in strs[j]:
                        count_j[ord(s) - ord("a")] += 1

                    if count_j == count_i:
                        group.append(strs[j])
                        visited[j] = True
            result.append(group)
        return result
    # endregion
    
    # region: solution # 2: Optimization #1
    # Time Complexity: O(n * k log k) k = average string length
    # Space Complexity: O(n*k)
    def s2_groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            # key = tuple(sorted(word))
            groups[key].append(word)
            
        return list(groups.values())
    # endregion

    # region: solution # 3: Optimization #2
    # Time Complexity: O(n * k) k = average string length
    # Space Complexity: O(n*k)
    def s3_groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord("a")] += 1

            groups[tuple(count)].append(word)
            
        return list(groups.values())
    # endregion

    # region: solution # 4: Optimization #3
    # Time Complexity: O(n * k) k = average string length
    # Space Complexity: O(n*k)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            frequency = {}
            for char in word:
                frequency[char] = frequency.get(char, 0) + 1
            groups[frozenset(frequency.items())].append(word)
        return list(groups.values())
    # endregion

def test():
    test_cases = [
        {
            "strs": ["eat", "tea", "tan", "ate", "nat", "bat"],
            "expected": [
                ["eat", "tea", "ate"],
                ["tan", "nat"],
                ["bat"]
            ]
        },
        {
            "strs": [""],
            "expected": [[""]]
        },
        {
            "strs": ["a"],
            "expected": [["a"]]
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):
        result = solution.groupAnagrams(tc["strs"])

        print(f"Test Case {i}")
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()

if __name__ == "__main__":
    test()