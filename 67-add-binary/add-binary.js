/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    const parseSum = BigInt(`0b${a}`) + BigInt(`0b${b}`)
    return parseSum.toString(2)
};