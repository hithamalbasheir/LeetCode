# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        curr = head
        while curr.next:
            next_node = curr.next
            num = gcd(next_node.val, curr.val)
            curr.next = ListNode(val = num, next = next_node)
            curr = next_node
        return head
        