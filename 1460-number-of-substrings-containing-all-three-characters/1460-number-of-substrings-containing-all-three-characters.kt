class Solution {
    fun numberOfSubstrings(s: String): Int {
        var left = 0
        var res = 0
        var charsMap = mutableMapOf<Char, Int>()
        for (right in 0 until s.length) {
            charsMap[s[right]] = charsMap.getOrDefault(s[right], 0) + 1
            while (charsMap.size == 3) {
                res += s.length - right
                charsMap[s[left]] = charsMap[s[left]]!! - 1
                if (charsMap[s[left]] == 0) {
                    charsMap.remove(s[left])
                }
                left++
            }
        }
        return res
    }
}