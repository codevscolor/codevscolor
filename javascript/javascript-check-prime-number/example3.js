// https://codevscolor.com/javascript-check-prime-number

function isPrime(num) {
  if (num < 2 || isNaN(num) || !isFinite(num)) return false;
  if (num % 2 == 0) return num == 2;

  for (let i = 3; i <= Math.sqrt(num); i += 2) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

console.log(isPrime(2));
console.log(isPrime(53));