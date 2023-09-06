# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        counter = 0
        curr = head
        while curr:
            counter += 1
            curr = curr.next
        part = counter // k if counter > k else 1
        extra = counter % k if counter > k else 0
        res = [None] * k
        cur = head
        prev = None
        for i in range(k):

            res[i] = cur

            for i in range(part +(1 if extra > 0 else 0)):
                prev = cur
                if cur:
                    cur = cur.next

            if prev:
                prev.next = None
            
            extra -= 1

            
        return res
                
