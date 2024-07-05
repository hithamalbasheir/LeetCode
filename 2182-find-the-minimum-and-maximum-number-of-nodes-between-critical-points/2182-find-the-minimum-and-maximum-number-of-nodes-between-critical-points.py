# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, curr, ahead = head, head.next, head.next.next
        if not ahead: return [-1, -1]
        criticals = []
        minima = float('inf')
        pos = 2
        while ahead:
            if curr.val < ahead.val and curr.val < prev.val:
                if criticals: minima = min(minima, pos - criticals[-1])
                criticals.append(pos)
            elif curr.val > ahead.val and curr.val > prev.val:
                if criticals: minima = min(minima, pos - criticals[-1])
                criticals.append(pos)
            ahead = ahead.next
            curr = curr.next
            prev = prev.next
            pos += 1
        if len(criticals) >= 2:
            return [minima, criticals[-1] - criticals[0]]
        return [-1, -1]