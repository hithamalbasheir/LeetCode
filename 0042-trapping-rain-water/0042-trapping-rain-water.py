class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i, e in enumerate(height):
            # we need to see if we can form a container
            while stack and e >= stack[-1][0]:
                popped, _ = stack.pop()
                # is it a container though? we have a left border?
                if stack:
                    left_border, j = stack[-1]
                    # we compute the water
                    water += min(left_border - popped, e - popped)*(i-j-1)
            stack.append((e,i))
        return water