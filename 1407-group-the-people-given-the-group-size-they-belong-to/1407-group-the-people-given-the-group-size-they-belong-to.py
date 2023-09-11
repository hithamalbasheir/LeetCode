class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mapping = {}
        for i, j in enumerate(groupSizes):
            if j in mapping:
                mapping[j].append(i)
            else:
                mapping[j] = [i]
        result = []
        for size, indices in mapping.items():
            for i in range(0, len(indices), size):
                result.append(indices[i:i+size])
        return result