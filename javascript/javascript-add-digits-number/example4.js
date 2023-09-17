// https://codevscolor.com/javascript-add-digits-number

let n = 679;

let initialValue = 0;
let sum = String(n).split('').reduce((accumulator, currentValue) => accumulator + Number(currentValue), initialValue);

console.log(`Sum of digits of ${n}: ${sum}`);