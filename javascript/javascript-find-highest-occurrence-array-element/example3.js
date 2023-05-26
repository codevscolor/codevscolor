// https://codevscolor.com/javascript-find-highest-occurrence-array-element

const givenArray = [1, 2, 3, 4, 1, 1, 2, 3, 4];

const maxValue = givenArray
  .sort(
    (previous, current) =>
      givenArray.filter((item) => item === previous).length -
      givenArray.filter((item) => item === current).length
  )
  .pop();

console.log(`Maximum occurrence value: ${maxValue}`);