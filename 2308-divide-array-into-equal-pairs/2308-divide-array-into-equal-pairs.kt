class Solution {
    fun divideArray(nums: IntArray): Boolean {
        var memo = mutableMapOf<Int, Int>().withDefault {0}
        for (num in nums) {
            memo[num] = memo.getValue(num) + 1
        }
        memo.forEach {
            if (it.value % 2 == 1) {
                return false
            }
        }
        return true
    }
}