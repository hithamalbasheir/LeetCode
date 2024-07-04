# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        head = head.next
        while head:
            if head.val == 0:
                if head.next: 
                    curr.next = ListNode()
                    curr = curr.next
                head = head.next
                continue
            curr.val += head.val
            head = head.next
        return res