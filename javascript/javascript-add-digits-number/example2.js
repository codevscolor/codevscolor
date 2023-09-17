// https://codevscolor.com/javascript-add-digits-number

let n = 679;
let sum = 0;

for(let no = n; no > 0; no = Math.floor(no/10)){
    sum += no % 10;
}

console.log(`Sum of digits of ${n}: ${sum}`);