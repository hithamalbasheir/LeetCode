class Solution {
    fun coloredCells(n: Int): Long {
        var res: Long = 1
        var inc = 4
        for (i in 1 until n) {
            res += inc
            inc += 4
        }
        return res
    }
}