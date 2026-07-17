from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    # region: Brute force
    """ Read every value. Store values in an array. Build a new linked list in reverse order.
    Let: n = length of nodes
    Time Complexity: 
    - First traversal: O(n)
    - Building the new list: O(n)
    - Overall: O(n) + O(n) = O(2n)
    Space Complexity: 
    - The values list stores "n" values: O(n)
    """
    def s1_reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next
        
        dummy = ListNode()
        current = dummy

        for value in values[::-1]:
        # for value in reversed(values):
            current.next = ListNode(value)
            current = current.next
        
        return dummy.next
    # endregion

    # region: Optimization #1
    """ Recursive
    Let: n = length of nodes
    Time Complexity: 
    - Overall: O(n)
    Space Complexity: 
    - Overall (Stack Space): O(n)
    """
    def s2_reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.s2_reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
    # endregion

    # region: Optimization #1
    """ Use three pointers (iterative)
    Let: n = length of nodes
    Time Complexity: 
    - Every node is visited exactly once: O(n)
    Space Complexity: 
    - Only store three pointers:: O(1)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        return previous
    # endregion

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


def test():
    test_cases = [
        {
            "head": [1, 2, 3, 4, 5],
            "expected": [5, 4, 3, 2, 1]
        },
        {
            "head": [1, 2],
            "expected": [2, 1]
        },
        {
            "head": [],
            "expected": []
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start=1):

        head = build_linked_list(tc["head"])

        result = solution.reverseList(head)

        actual = linked_list_to_list(result)

        print(f"Test Case {i}")
        print("Input:", tc["head"])
        print("Expected:", tc["expected"])
        print("Actual:", actual)
        print()


if __name__ == "__main__":
    test()