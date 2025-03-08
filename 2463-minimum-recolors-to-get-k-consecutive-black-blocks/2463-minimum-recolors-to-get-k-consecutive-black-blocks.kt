class Solution {
    fun minimumRecolors(blocks: String, k: Int): Int {
        var whites = 0
        var blacks = 0
        for (i in 0 until k) {
            when (blocks[i]) {
                'W' -> whites++
                'B' -> blacks++
            }
        }
        var res = whites //Worst case scenario would be that the whole array is whites
        for (i in k until blocks.length) {
            when (blocks[i]) {
                'W' -> whites++
                'B' -> blacks++
            } 
            
            when (blocks[i - k]) {
                'W' -> whites--
                'B' -> blacks--
            } 
            res = min(whites, res)
        }
        return res
    }
}