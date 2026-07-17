Solve LeetCode <problem number>: <problem name>

Provide the answer in the following format:

# 1. Repository Structure

Suggest the folder location for this problem.

Example:

neetcode75/
├── arrays_hashing/
│   └── 0001_two_sum.py

Explain why this category is appropriate.

# 2. GitHub Filename

Follow this naming convention:

<4-digit-problem-number>_<problem_name_snake_case>.py

Examples:

0001_two_sum.py
0217_contains_duplicate.py
0347_top_k_frequent_elements.py

# 3. Boilerplate Python File

Generate a complete runnable Python file containing:

- Imports
- LeetCode Solution class
- Empty solution method signature
- test() function
- main execution block

Example format:

from typing import List

class Solution:
    def twoSum(
        self,
        nums: List[int],
        target: int
    ) -> List[int]:

        pass


def test():

    test_cases = [
        {
            "nums": [2,7,11,15],
            "target": 9,
            "expected": [0,1]
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        result = solution.twoSum(
            tc["nums"],
            tc["target"]
        )

        print(f"Test Case {i}")
        print("Expected:", tc["expected"])
        print("Actual:", result)
        print()


if __name__ == "__main__":
    test()

Do NOT implement the solution yet.

# 4. Pattern Recognition

- Category
- Difficulty
- Pattern
- Similar Problems

# 5. Interview Clues

What clues in the problem statement should immediately suggest this pattern?

# 6. Brute Force Solution

## Intuition

## Algorithm

## Python Solution

## Complexity

Time:
Space:

# 7. Optimization #1

## Why Brute Force Is Slow

## Improved Idea

## Python Solution

## Complexity

Time:
Space:

# 8. Optimization #2 (if applicable)

Repeat only if a meaningful optimization exists.

# 9. Optimal Solution

## Intuition

## Algorithm

## Python Solution

Interview-quality code.

## Complexity

Time:
Space:

# 10. Dry Run

Use a sample test case.

Show:

- Variables
- Data structures
- Pointer movement
- Decisions made

# 11. Alternative Approaches

Mention other valid solutions.

Include complexity comparison.

# 12. Common Mistakes

What mistakes do candidates typically make?

# 13. Edge Cases

List important edge cases.

Examples:

- Empty input
- Single element
- Duplicate values
- Sorted input
- Negative numbers

Explain which edge cases matter for this problem.

# 14. Follow-Up Questions

Possible interviewer follow-ups.

# 15. Revision Notes

Pattern:
When to use:
Key idea:
Complexity:
Related problems:

Keep this section under 10 lines.

# 16. NeetCode Mapping

List 3-5 NeetCode problems using the same pattern.

# 17. Data Engineer Interview Perspective

- Asked in DE interviews?
- FAANG frequency?
- Most important takeaway?
- Real-world data engineering application?

Examples:

Sliding Window → Event streams
Heap → Top-K analytics
Intervals → Sessionization
Graphs → Dependency lineage
Binary Search → Partitioning