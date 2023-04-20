// https://codevscolor.com/javascript-reverse-number

function reverseNumber(num) {
  return parseInt(num.toString().split("").reverse().join(""));
}

let num = 768493;
let rev = reverseNumber(num);

console.log("Reverse number : " + rev);
