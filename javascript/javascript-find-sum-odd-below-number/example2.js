// https://codevscolor.com/javascript-find-sum-odd-below-number
function isOdd(n) {
  return Boolean(n % 2);
}

function findSum(no) {
  let sum = 0,
    i = 0;

  while (i < no) {
    if (isOdd(i)) {
      sum += i;
    }
    i++;
  }
  return sum;
}

console.log(findSum(100));
