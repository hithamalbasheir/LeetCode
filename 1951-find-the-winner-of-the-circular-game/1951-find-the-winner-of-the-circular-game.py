class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #Simulation
        ppl = [i for i in range(1, n + 1)]
        idx = 0
        while len(ppl) > 1:
            remove = (idx + k - 1) % len(ppl)
            ppl.pop(remove)
            idx = remove
        return ppl[0]