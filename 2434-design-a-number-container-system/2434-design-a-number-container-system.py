class NumberContainers:

    def __init__(self):
        self.numbers_indices = defaultdict(SortedSet)
        self.idx_num = {}

    def change(self, index: int, number: int) -> None:
        if index in self.idx_num:
            prev_number = self.idx_num[index]
            self.numbers_indices[prev_number].remove(index)

            if len(self.numbers_indices[prev_number]) == 0:
                del self.numbers_indices[prev_number]
            
        self.idx_num[index] = number
        self.numbers_indices[number].add(index)
        
    def find(self, number: int) -> int:
        if number in self.numbers_indices:
            return self.numbers_indices[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)