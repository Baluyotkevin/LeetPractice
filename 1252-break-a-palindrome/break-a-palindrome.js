/**
 * @param {string} palindrome
 * @return {string}
 */
var breakPalindrome = function(palindrome) {
    if (palindrome.length < 2) return ""
    let str = ""
    for (let i = 0; i < palindrome.length; i++) {
        if (palindrome[i] != 'a') {
            str += 'a'
            str += palindrome.slice(0, i) + palindrome.slice(i + 1)
            let reverseStr = str.split('').reverse().join('')
            if (str !== reverseStr) {
                return str
            }
        }
    }
    return palindrome.slice(0, palindrome.length - 1) + 'b'
};