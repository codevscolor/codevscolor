// https://codevscolor.com/javascript-find-sum-even-below-number

function isEven(n) {
  return n % 2 == 0;
}

function findSum(no) {
  let sum = 0;

  for (var i = 1; i <= no; i++) {
    if (isEven(i)) {
      sum += i;
    }
  }
  return sum;
}

console.log(findSum(100));
