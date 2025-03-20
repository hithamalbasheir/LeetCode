class UnionFind (n: Int) {
    val parent = IntArray(n) {it -> it}
    val size = IntArray(n) {_ -> 1}

    fun find(x: Int): Int {
        if (x != parent[x]) {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }
    
    fun union(a: Int, b: Int) {
        val x = find(a)
        val y = find(b)
        if (x == y) {
            return
        }
        if (size[x] > size[y]) {
            parent[y] = x
            size[x] += size[y]
        } else {
            parent[x] = y
            size[y] += size[x]
        }
    }
}


class Solution {
    fun minimumCost(n: Int, edges: Array<IntArray>, query: Array<IntArray>): IntArray {
        val uf = UnionFind(n)
        edges.forEach {
            (src: Int, dest: Int, _: Int) ->
            uf.union(src, dest)
        }

        val componentCost = mutableMapOf<Int, Int>()
        edges.forEach {
            (src, dest, w) ->
            val root = uf.find(src)
            if (root !in componentCost) {
                componentCost[root] = w
            } else {
                componentCost[root] = componentCost[root]!!.and(w)
            }
        }
        val res = IntArray(query.size)
        query.forEachIndexed {
            i, (src: Int, dest: Int) -> 
            val v1 = uf.find(src)
            val v2 = uf.find(dest)
            if (v1 == v2) {
                res[i] = componentCost[v1]!!
            } else {
                res[i] = -1
            }
        }
        return res
    }
}