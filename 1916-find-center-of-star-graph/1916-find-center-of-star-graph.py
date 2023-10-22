class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        #Since we know that there will always be one common number, we can just return the common element between the first two of them by this one liner comparison
        return edges[0][0] if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1] else edges[0][1]
        