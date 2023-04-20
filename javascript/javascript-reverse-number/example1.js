// https://codevscolor.com/javascript-reverse-number

let rev = 0;
let num = 123456;
let lastDigit;

while(num != 0){
  lastDigit = num % 10;
  rev = rev * 10 + lastDigit;
  num = Math.floor(num/10);
}

console.log("Reverse number : "+rev);