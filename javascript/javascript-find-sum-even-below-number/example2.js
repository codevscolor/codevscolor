// https://codevscolor.com/javascript-find-sum-even-below-number

function isEven(n) {
  return n % 2 == 0;
}

function findSum(no) {
  let sum = 0;
  let i = 1;

  while (i <= no) {
    if (isEven(i)) {
      sum += i;
    }
    i++;
  }
  return sum;
}

console.log(findSum(100));
