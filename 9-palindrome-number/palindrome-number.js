/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let b = x.toString().split('').reverse().join('')
    return x.toString() === b
};