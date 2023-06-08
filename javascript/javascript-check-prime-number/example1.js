// https://codevscolor.com/javascript-check-prime-number

function isPrime(num) {
  if (num < 2 || isNaN(num) || !isFinite(num)) return false;

  for (let i = 2; i <= num / 2; i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

console.log(isPrime(2));
console.log(isPrime(53));