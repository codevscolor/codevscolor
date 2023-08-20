// https://codevscolor.com/javascript-check-element-is-in-array

const isInArray = (arr, n) => {
    return arr.includes(n);
}

console.log(`2 is in [1, 2, 3, 4, 5, 6]: ${isInArray([1, 2, 3, 4, 5, 6], 2)}`);
console.log(`7 is in [1, 2, 3, 4, 5, 6]: ${isInArray([1, 2, 3, 4, 5, 6], 7)}`);