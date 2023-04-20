// https://codevscolor.com/javascript-reverse-number

function reverseNumber(num) {
  return (
    parseFloat(num.toString().split("").reverse().join("")) * Math.sign(num)
  );
}

let num = 123.45;
let rev = reverseNumber(num);

console.log("Reverse number : " + rev);
