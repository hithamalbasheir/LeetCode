class Solution {
    fun numberOfAlternatingGroups(colors: IntArray, k: Int): Int {
        //Sliding window
        var left = 0
        var right = 1
        var n = colors.size
        var res = 0
        while (right < n + k - 1) {
            if(colors[right % n] == colors[(right - 1) % n]) {
                left = right
            }
            if ((right - left) < (k - 1)) {
                right += 1
            }
            else {
                println("l $left r $right")
                res += 1
                left += 1
            }
        }
        return res
    }
}