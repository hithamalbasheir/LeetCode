class Solution {
    fun findMissingAndRepeatedValues(grid: Array<IntArray>): IntArray {
        var seen = mutableSetOf<Int>()
        var res = IntArray(2)
        grid.forEach {
            it.forEach {
                if (it in seen) {
                    res[0] = it
                }
                seen.add(it)
            }
        }
        var n = grid.size
        for (i in 1..n*n) {
            if (i !in seen) {
                res[1] = i
                return res
            }
        }
        return res
    }
}