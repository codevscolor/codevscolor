// https://codevscolor.com/javascript-check-element-is-in-array

const isInArray = (arr, n, from) => {
    return arr.includes(n, from);
}

const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

console.log(`Search for 3 starting index 3: ${isInArray(arr, 3, 3)}`);
console.log(`Search for 3 starting index 1: ${isInArray(arr, 3, 1)}`);