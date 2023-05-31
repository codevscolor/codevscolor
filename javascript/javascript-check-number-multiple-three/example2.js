// https://codevscolor.com/javascript-check-number-multiple-three
const isMultipleOfThree = (num) => {
  if (num === 0) return true;
  if (num < 0) return false;

  return isMultipleOfThree(num - 3);
};

for (let i = 0; i <= 30; i++) {
  if (isMultipleOfThree(i)) {
    console.log(i);
  }
}
