class Solution {
    fun minZeroArray(nums: IntArray, queries: Array<IntArray>): Int {
        var n = nums.size
        var sum = 0
        var res = 0
        var diffArray = IntArray(n + 1)
        for (i in 0 until n) {
            while (sum + diffArray[i] < nums[i]) {
                res++

                if (res > queries.size) {
                    return -1
                }

                var left = queries[res - 1][0]
                var right = queries[res - 1][1]
                var change = queries[res - 1][2]

                if (right >= i) {
                    diffArray[max(left, i)] += change
                    diffArray[right + 1] -= change
                }
            }
            sum += diffArray[i]
        }
        return res
    }
}