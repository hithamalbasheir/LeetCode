class Solution {
    fun minCapability(nums: IntArray, k: Int): Int {
        //Very cool way to apply binary search, although I haven't thought about it
        var left: Int = 1000_000_000
        var right = 1
        for (num in nums) {
            left = min(left, num)
            right = max(right, num)
        }
        fun checkValidity(check: Int): Boolean {
            var count = 0
            var i = 0
            while (i < nums.size) {
                if (nums[i] <= check) {
                    count++
                    i++
                }
                i++
            }
            return (count >= k)
        }
        while (left < right) {
            var mid = left + (right - left) / 2
            if (checkValidity(mid)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}