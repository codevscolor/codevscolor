// https://codevscolor.com/javascript-check-prime-number

function isPrime(num) {
  if (num < 2 || isNaN(num) || !isFinite(num)) return false;
  if (num % 2 == 0) return num == 2;
  if (num % 3 == 0) return num == 3;

  for (let i = 5; i <= Math.sqrt(num); i += 6) {
    if (num % i == 0 || num % (i + 2) == 0) {
      return false;
    }
  }
  return true;
}

console.log(isPrime(2));
console.log(isPrime(53));
