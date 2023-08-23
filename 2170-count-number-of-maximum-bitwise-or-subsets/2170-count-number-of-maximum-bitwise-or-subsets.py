class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        #Since the input is all positive the max_possible is the Bitwise OR of all elements in the array
        def get_bitwise_or(nums):
            bitwise_sum = 0
            for i in nums:
                bitwise_sum |= i
            return bitwise_sum
        max_possible = get_bitwise_or(nums)
        res = 0

        def dfs(depth, sub):
            nonlocal res
            if depth >= len(nums):
                bit_sum = get_bitwise_or(sub)
                if bit_sum == max_possible:
                    res += 1
                return
            
            sub.append(nums[depth])
            dfs(depth+1, sub)

            sub.pop()
            dfs(depth+1, sub)
        
        dfs(0, [])
        return res