class Solution {
    fun mergeArrays(nums1: Array<IntArray>, nums2: Array<IntArray>): Array<IntArray> {
        //Two pointers
        var ptr1 = 0
        var ptr2 = 0
        var res = mutableListOf<IntArray>()
        while (ptr1 < nums1.size && ptr2 < nums2.size ) {
            if (nums1[ptr1][0] == nums2[ptr2][0]) {
                var curr = nums1[ptr1][1] + nums2[ptr2][1]
                res.add(intArrayOf(nums1[ptr1][0], curr))
                ptr1++
                ptr2++
                continue
            } 
            if (nums1[ptr1][0] < nums2[ptr2][0]) {
                res.add(nums1[ptr1])
                ptr1++
            } else {
                res.add(nums2[ptr2])
                ptr2++
            }
        }

        while (ptr1 < nums1.size) {
            res.add(nums1[ptr1])
            ptr1++
        }

        while (ptr2 < nums2.size) {
            res.add(nums2[ptr2])
            ptr2++
        }
        return res.toTypedArray()
    }
}