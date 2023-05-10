// https://codevscolor.com/javascript-find-sum-odd-below-number
function findSum(no) {
  let sum = 0,
    i = 1;

  while (i < no) {
    sum += i;
    i += 2;
  }
  return sum;
}

console.log(findSum(100));
