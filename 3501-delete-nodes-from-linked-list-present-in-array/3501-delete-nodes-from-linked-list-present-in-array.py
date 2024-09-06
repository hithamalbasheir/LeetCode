# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        nums = set(nums)
        curr = dummy.next
        prev = dummy
        while curr:
            if curr.val in nums:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next