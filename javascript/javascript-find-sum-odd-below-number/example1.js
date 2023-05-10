// https://codevscolor.com/javascript-find-sum-odd-below-number
function isOdd(n) {
  return Boolean(n % 2);
}

function findSum(no) {
  let sum = 0;

  for (var i = 0; i < no; i++) {
    if (isOdd(i)) {
      sum += i;
    }
  }
  return sum;
}

console.log(findSum(100));
