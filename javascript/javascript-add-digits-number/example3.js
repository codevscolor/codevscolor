// https://codevscolor.com/javascript-add-digits-number

let n = 679;
let sum = 0;

String(n).split('').forEach(e => sum += Number(e));

console.log(`Sum of digits of ${n}: ${sum}`);