// https://codevscolor.com/javascript-find-object-is-in-array

let a1 = [1, 2, 3, 4]; // true
let a2 = [{i: 1}, 2, 3]; // true
let a3 = 5; // false
let a4 = 'hello'; // false
let a5 = undefined; // false
let a6 = {'name': 'Alex'}; // false

console.log(a1 instanceof Array);
console.log(a2 instanceof Array);
console.log(a3 instanceof Array);
console.log(a4 instanceof Array);
console.log(a5 instanceof Array);
console.log(a6 instanceof Array);