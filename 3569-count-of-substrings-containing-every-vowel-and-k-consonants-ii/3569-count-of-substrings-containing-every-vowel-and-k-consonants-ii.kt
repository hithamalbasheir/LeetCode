class Solution {
    fun countOfSubstrings(word: String, k: Int): Long {
        fun atLeastK(k: Int): Long {
            var left = 0
            var res: Long = 0
            var vowels_map = mutableMapOf<Char, Int>()
            var k_count = 0
            var found_vowels = 0
            for (right in 0 until word.length) {
                var curr = word[right]
                if (curr in "aeiou") {
                    var curr_cnt = vowels_map.getOrDefault(curr, 0)
                    if (curr_cnt == 0) {
                        found_vowels++
                    }
                    vowels_map[curr] = curr_cnt + 1
                } else {
                    k_count++
                }
                while (k_count >= k && found_vowels == 5) {
                    res += (word.length - right)
                    curr = word[left]
                    if (curr in "aieou") {
                        vowels_map[curr] = vowels_map[curr]!! - 1
                        if (vowels_map[curr] == 0) {
                            found_vowels-- 
                        }
                    } else {
                        k_count--
                    }
                    left++
                } 
            }
            return res
        }
        
        return atLeastK(k) - atLeastK(k + 1) 
    }
}