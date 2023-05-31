// https://codevscolor.com/javascript-check-number-multiple-three
const sumDigits = (num) => {
  let sum = 0;
  while (num) {
    sum += num % 10;
    num = Math.floor(num / 10);
    if (num == 0 && sum > 9) {
      num = sum;
      sum = 0;
    }
  }
  return sum;
};

const isMultipleOfThree = (num) => {
  let sumOfDigits = sumDigits(num);
  return (
    sumOfDigits === 0 ||
    sumOfDigits === 3 ||
    sumOfDigits === 6 ||
    sumOfDigits === 9
  );
};

for (let i = 0; i <= 100; i++) {
  if (isMultipleOfThree(i)) {
    console.log(i);
  }
}
