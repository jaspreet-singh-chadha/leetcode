# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final_list = dummyHead = ListNode(-1)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                final_list.next = l1
                l1 = l1.next
            else:
                final_list.next = l2
                l2 = l2.next

            final_list = final_list.next

        if l1 is not None:
            final_list.next = l1
        elif l2 is not None:
            final_list.next = l2

        return dummyHead.next


if __name__ == '__main__':

    def create_linked_list(list_values:list) -> Optional[ListNode]:
        linked_list = head = ListNode(list_values[0])

        for val in list_values[1:len(list_values)]:
            linked_list.next = ListNode(val)
            linked_list = linked_list.next

        return head

    def print_linked_list(linked_list: Optional[ListNode]):
        temp_list = []
        while linked_list is not None:
            temp_list.append(linked_list.val)
            linked_list = linked_list.next

        print(temp_list)

    test_linked_list = create_linked_list([1,2,4])

    merged_list = Solution().mergeTwoLists(l1=create_linked_list([1, 2, 4, 6]), l2=create_linked_list([1, 3, 4, 5]))
    print_linked_list(merged_list)