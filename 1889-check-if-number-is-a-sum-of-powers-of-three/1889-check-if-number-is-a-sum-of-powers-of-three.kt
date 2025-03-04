class Solution {
    fun checkPowersOfThree(n: Int): Boolean {
        var n = n
        var i = 0
        val BASE = 3.0
        while ((BASE.pow(i+1)) <= n) {
            i++
        }

        while (n > 0 && i >= 0) {
            var power = (BASE.pow(i))
            if (power <= n) {
                n -= power.toInt()
            }
            i -= 1
        }
        print(n)
        return n == 0
    }
}