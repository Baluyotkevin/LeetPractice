/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    const arr = []
    const arr2 = []
    for (let i = 0; i < nums1.length; i++) {
        if (!nums2.includes(nums1[i]) && !arr.includes(nums1[i])) {
            arr.push(nums1[i])
        }
    }
    console.log(arr)
    for (let j = 0; j < nums2.length; j++) {
        if (!nums1.includes(nums2[j]) && !arr2.includes(nums2[j])) {
            arr2.push(nums2[j])
        }
    }

    return [arr, arr2]
};