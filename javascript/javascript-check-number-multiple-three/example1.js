// https://codevscolor.com/javascript-check-number-multiple-three
const isMultipleOfThree = (num) => {
  const div = parseInt(num / 3);

  return num === div * 3;
};

for (let i = 0; i <= 30; i++) {
  if (isMultipleOfThree(i)) {
    console.log(i);
  }
}
