# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse_linked_list(head, k):
            current = head
            previous = None
            for _ in range(k):
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            return previous, current
        dummy = ListNode(0, head)
        current = dummy
        k = right - left + 1
        i = 0
        while current:
            if i == left:
                previous.next, current.next = reverse_linked_list(current, k)
                break
            i += 1
            previous = current
            current = current.next
        return dummy.next