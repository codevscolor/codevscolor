// https://codevscolor.com/javascript-check-prime-number

function isPrime(num) {
  if (num <= 1) return false;
  if (num == 2) return true;

  for (let i = 2; i <= num / 2; i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

let result = [];

for (let j = 1; j <= 100; j++) {
  if (isPrime(j)) {
    result.push(j);
  }
}

console.log(result);
