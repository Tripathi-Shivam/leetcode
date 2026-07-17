from typing import List

class Solution:
    # region: solution # 1: Brute force
    """ HashMap
    Let: n = total numbers & m = unique numbers
    Time Complexity: 
    - Counting Frequencies: O(n)
    - Finding the maximum: O(m)
    - Reapeated k times: O(km)
    - Overall: O(n + km)
    - Worst case: O(n²) (because: m = n & k = n)
    Space Complexity: 
    - Frequency map: O(m)
    - Worst case: O(n)
    """
    def s1_topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        result = []
        for _ in range(k):
            max_num = None
            max_freq = -1

            for num, freq in frequency.items():
                if freq > max_freq:
                    max_num = num
                    max_freq = freq
            
            result.append(max_num)
            del frequency[max_num]

        return result
    # endregion

    # region: solution # 2: Optimization #1
    """ Sorting
    Let: n = total numbers & m = unique numbers
    Time Complexity: 
    - Counting Frequencies: O(n)
    - Sort "m" unique elements: O(m log m)
    - Overall: O(n + m log m)
    - Worst case: O(n log n) (because: m = n & k = n)
    Space Complexity: 
    - Frequency map: O(m)
    - Sorted list: O(m)
    - Overall: O(n)
    """
    def s2_topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        sorted_items = sorted(
            frequency.items(),
            key = lambda item: item[1],
            reverse = True
        )

        return [num for num, freq in sorted_items[:k]]
    # endregion

    # region: solution # 3: Optimization #2
    """ Min Heap (maintain a min-heap of size k)
    Let: n = total numbers & m = unique numbers
    Time Complexity: 
    - Counting Frequencies: O(n)
    - Each push/pop: O(log k)
    - Performed "m" times: O(m log k)
    - Overall: O(n + m log k)
    - Worst case: O(n log k) (because: m = n)
    Space Complexity: 
    - Frequency map: O(m)
    - Heap: O(k)
    - Overall: O(n)
    """
    def s3_topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        heap = []

        for num, freq in frequency.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap) # removing num with minimum frequency

        return [num for freq, num in heap]
    # endregion

    # region: solution # 4: Optimization #3
    """ Bucket Sort (create bucket indexed by frequency)
    Let: n = total numbers & m = unique numbers
    Time Complexity: 
    - Counting Frequencies: O(n)
    - Building buckets: O(m)
    - Scanning buckets: O(n)
    - Overall: O(n)
    Space Complexity: 
    - Frequency map: O(m)
    - Buckets: O(n)
    - Overall: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in frequency.items():
            buckets[freq].append(num)

        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
    # endregion


def test():
    test_cases = [
        {
            "nums": [1, 1, 1, 2, 2, 3],
            "k": 2,
            "expected": [1, 2]
        },
        {
            "nums": [1],
            "k": 1,
            "expected": [1]
        },
        {
            "nums": [4, 4, 4, 6, 6, 1],
            "k": 1,
            "expected": [4]
        },
        {
            "nums": [1,2,1,2,1,2,3,1,3,2],
            "k": 2,
            "expected": [1,2]
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start = 1):
        result = solution.topKFrequent(tc["nums"], tc["k"])

        print(f"Test Case {i}")
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()

if __name__ == "__main__":
    test()