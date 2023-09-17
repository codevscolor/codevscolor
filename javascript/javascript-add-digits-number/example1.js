// https://codevscolor.com/javascript-add-digits-number

let n = 234;
let sum = 0;

let no = n;
while(no){
    sum += no % 10;
    no = Math.floor(no/10);
}

console.log(`Sum of digits of ${n}: ${sum}`);