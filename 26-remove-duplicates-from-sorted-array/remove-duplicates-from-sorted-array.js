/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    const newArr = new Set(nums)
    const newNewArr = Array.from(newArr)
    for (let i = 0; i < newNewArr.length; i++) {
        nums[i] = newNewArr[i]
    }
    nums.length = newNewArr.length
    return nums.length
};