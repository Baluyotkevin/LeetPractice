/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // put into a key value pair for objects;
    // maybe a double loop?
    // check to see if first and last are open and closed
    const stack = [];

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '{') {
            stack.push('}')
        }
        else if (s[i] === '[') {
            stack.push(']')
        }
        else if (s[i] === '(') {
            stack.push(')')
        }
        else if (stack.pop() !== s[i]) {
            return false
        }
    }
    return !stack.length
};