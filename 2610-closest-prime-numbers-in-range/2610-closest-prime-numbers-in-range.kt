class Solution {
    fun closestPrimes(left: Int, right: Int): IntArray {
        //Using Sieve of Eratosthenes - cool name :)
        fun getPrimes(): MutableList<Int> {
            var primes = BooleanArray(right + 1) { it > 1 }
            var upperBound = sqrt(right.toFloat()).toInt()
            for (i in 2..upperBound) {
                if (!primes[i]) {
                    continue
                }
                for (j in i * 2 .. right step i) {
                    primes[j] = false
                }
            }
            

            var primeNums = mutableListOf<Int>()
            for (i in left..right) {
                if (primes[i]) {
                    primeNums.add(i)
                }
            }

            primeNums.forEach {
                print(it)
            }

            return primeNums
        }

        var primeNums = getPrimes()
        if (primeNums.size < 2) {
            return IntArray(2) {-1}
        } 
        var res = IntArray(2)
        var diff = right + 1
        for (i in 1..< primeNums.size) {
            var currDiff = (primeNums[i] - primeNums[i - 1])
            if (currDiff < diff) {
                res[0] = primeNums[i - 1]
                res[1] = primeNums[i]
                diff = currDiff
            }
        }
        return res
    }
}