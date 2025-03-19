class Solution {
    fun minOperations(nums: IntArray): Int {
        var res = 0
        var n = nums.size
        for (i in 0 until n) {
            if (i > n - 3) {
                if (nums[i] == 0) {
                    return -1
                }
            }
            if (nums[i] == 1) {
                continue
            }
            for (j in i until i + 3) {
                nums[j] = abs(nums[j] - 1)
            }
            res++
        }
        return res
    }
}