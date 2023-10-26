/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map()
    // { 2: 1,  }
    for (let i = 0; i < nums.length; i++) {
        let num = target - nums[i]
        if (map.has(num)) {
            return [i, map.get(num)]
        } else {
            map.set(nums[i], i)
        }
    }
};