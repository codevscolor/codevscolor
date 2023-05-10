// https://codevscolor.com/javascript-find-sum-odd-below-number
function findSum(no) {
  let sum = 0;

  for (var i = 1; i < no; i += 2) {
    sum += i;
  }
  return sum;
}

console.log(findSum(100));
