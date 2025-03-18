class Solution {
    fun longestNiceSubarray(nums: IntArray): Int {
        var left = 0
        var right = 0
        var res = 1
        var bitMask = IntArray(32)
        var conflicts = 0
        while (right < nums.size) {
            var bitNum = Integer.toBinaryString(nums[right])
            bitNum.reversed().forEachIndexed {
                idx, bit ->
                if (bit != '0') {
                    if (bitMask[idx] >= 1) {
                        conflicts++

                    }
                    bitMask[idx]++
                }
            }
            right++
            while (conflicts > 0) {
                bitNum = Integer.toBinaryString(nums[left])
                bitNum.reversed().forEachIndexed {
                    idx, bit -> 
                    if (bit != '0') {
                        if (bitMask[idx] > 1) {
                            conflicts--
                        }
                        bitMask[idx]--
                    }
                }
                left++
            }
            res = max(res, right - left)
        }
        return res
    }
}