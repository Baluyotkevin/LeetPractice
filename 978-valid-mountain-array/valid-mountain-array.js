/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function(arr) {
      if (arr.length < 3) return false;

    let isGoingUp;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i+1] && arr[i+1] > arr[i] && (isGoingUp || isGoingUp === undefined)) {
            isGoingUp = true;
        } else if (arr[i+1] && arr[i+1] < arr[i] && isGoingUp) {
            isGoingUp = false;
        } else if (arr[i+1] && arr[i+1] < arr[i] && isGoingUp === false) {
            isGoingUp = false;
        } else if (arr[i+1]) {
            return false;
        }
    }
    
    return isGoingUp === false;
};