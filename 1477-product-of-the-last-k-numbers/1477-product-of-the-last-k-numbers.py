class ProductOfNumbers:
#Child's play, I'll just preprocess the product of the array, and divide it when I want the first K numbers, here this is O(1) for both adding and getting
    def __init__(self):
        self.nums = deque([])
        self.curr_product = deque([1])

    def add(self, num: int) -> None:
        if num == 0:
            self.__init__()
            return
        self.nums.append(num)
        self.curr_product.append(self.curr_product[-1] * num) 


    def getProduct(self, k: int) -> int:
        if len(self.curr_product) <= k:
            return 0
        return self.curr_product[-1] // self.curr_product[-k - 1]        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)