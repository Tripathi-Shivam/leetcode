from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass

def buildLinkedList(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    currNode = dummy

    for value in values:
        currNode.next = ListNode(value)
        currNode = currNode.next
    
    return dummy.next

def linkedListToList(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test():
    test_cases = [
        {
            "list1": [1, 2, 4],
            "list2": [1, 3, 4],
            "expected": [1, 1, 2, 3, 4, 4]
        },
        {
            "list1": [],
            "list2": [],
            "expected": []
        },
        {
            "list1": [],
            "list2": [0],
            "expected": [0]
        },
        {
            "list1": [5],
            "list2": [1, 2, 4],
            "expected": [1, 2, 4, 5]
        }
    ]

    solution = Solution()

    for i, tc in enumerate(test_cases, start = 1):
        list1 = buildLinkedList(tc["list1"])
        list2 = buildLinkedList(tc["list2"])

        result = solution.mergeTwoLists(list1, list2)

        actual = linkedListToList(result)

        print(f"Test Case {i}")
        print("List 1:", tc["list1"], "List 2:", tc["list2"])
        print("Expected:", tc["expected"])
        print("Actual:", actual)
        print()

if __name__ == "__main__":
    test()