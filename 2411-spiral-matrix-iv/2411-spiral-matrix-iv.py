# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        up, left = -1, -1
        curr = head
        i, j = 0, 0
        direction = "r"
        while curr:
            res[i][j] = curr.val
            curr = curr.next
            match direction:
                case 'r':
                    j += 1
                    if j == n:
                        direction = 'd'
                        up += 1
                        i += 1
                        j -= 1
                case 'd':
                    i += 1
                    if i == m:
                        direction = 'l'
                        n -= 1
                        j -= 1
                        i -= 1
                case 'l':
                    j -= 1
                    if j == left:
                        direction = 'u'
                        m -= 1
                        j += 1
                        i -= 1
                case 'u':
                    i -= 1
                    if i == up:
                        direction = 'r'
                        left += 1
                        j += 1
                        i += 1
        return res