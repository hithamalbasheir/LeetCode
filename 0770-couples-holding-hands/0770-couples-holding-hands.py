class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        dic = {j:i for i, j in enumerate(row)}

        count = 0
        for i in range(0, len(row), 2):
            if row[i] % 2 == 0:
                complement = row[i] + 1
            else:
                complement = row[i] - 1
            
            actual = row[i+1]
            if complement != actual:
                row[i+1], row[dic[complement]] = complement, actual
                dic[complement], dic[actual] = i+1, dic[complement]
                count += 1
        return count