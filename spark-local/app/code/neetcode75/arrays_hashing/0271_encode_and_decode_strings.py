from typing import List

class Codec:
    # region: solution # 1: Brute force
    """ Join using delimiter (not a valid solution)
    Let: T = total characters
    Time Complexity: 
    - Joining: O(T)
    - Spliting: O(T)
    Space Complexity: 
    - Overall: O(T)
    """
    def s1_encode(self, strs: List[str]) -> str:
        return "#".join(strs)

    def s2_decode(self, s: str) -> List[str]:
        return s.split("#")
    # endregion

    # region: solution # 2: Optimal Solution
    """ Store the length of every string
    Let: n = number of strings & T = total number of characters across all strings
    Time Complexity: 
    - Encoding Time: O(T) (we visit every character exactly once)
    - Decoding Time: O(T) (each character is read once)
    Space Complexity: 
    - Overall: O(T) (encoded string stores all original characters + length prefixes)
    - The length prefix is very small compared to the string itself.
    """
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += (str(len(word)) + "#" + word)

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            result.append(word)
            i = j + 1 + length

        return result
    # endregion

def test():
    test_cases = [
        {
            "strs": ["lint", "code", "love", "you"]
        },
        {
            "strs": [""]
        },
        {
            "strs": ["hello", "", "world"]
        },
        {
            "strs": ["helloworldhe#23lloworld", "", "world"]
        }
    ]

    codec = Codec()
    for i, tc in enumerate(test_cases, start = 1):
        encoded = codec.encode(tc["strs"])
        decoded = codec.decode(encoded)

        print(f"Test Case {i}")
        print("Original :", tc["strs"])
        print("Encoded  :", encoded)
        print("Decoded  :", decoded)
        print()

if __name__ == "__main__":
    test()