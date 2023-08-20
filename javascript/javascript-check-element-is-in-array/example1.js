// https://codevscolor.com/javascript-check-element-is-in-array

const isInArray = (arr, n) => {
    for(let i = 0; i < arr.length; i++){
        if(arr[i] === n) return true;
    }
    return false;
}

console.log(`2 is in [1, 2, 3, 4, 5, 6]: ${isInArray([1, 2, 3, 4, 5, 6], 2)}`);
console.log(`7 is in [1, 2, 3, 4, 5, 6]: ${isInArray([1, 2, 3, 4, 5, 6], 7)}`);