"""
----
Easy
----

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        if not list2:
            return

        return list2

    elif not list2:
        if not list1:
            return

        return list1

    l1_pointer = list1
    l2_pointer = list2

    if list1.val <= list2.val:
        list3 = ListNode(list1.val)
        l1_pointer = l1_pointer.next
    else:
        list3 = ListNode(list2.val)
        l2_pointer = l2_pointer.next

    l3_pointer = list3

    while (l1_pointer is not None) or (l2_pointer is not None):
        if l1_pointer is None:
            l3_pointer.next = l2_pointer
            break

        elif l2_pointer is None:
            l3_pointer.next = l1_pointer
            break

        else:
            if l1_pointer.val <= l2_pointer.val:
                l3_pointer.next = ListNode(l1_pointer.val)
                l3_pointer = l3_pointer.next
                l1_pointer = l1_pointer.next

            else:
                l3_pointer.next = ListNode(l2_pointer.val)
                l3_pointer = l3_pointer.next
                l2_pointer = l2_pointer.next

    return list3


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

l3 = merge_two_lists(l1, l2)
temp = l3

while temp:
    print(temp.val, end=" ")
    temp = temp.next
