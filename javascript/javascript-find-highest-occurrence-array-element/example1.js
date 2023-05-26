// https://codevscolor.com/javascript-find-highest-occurrence-array-element

const givenArray = [1, 2, 3, 4, 1, 1, 2, 3, 4];

let itemsMap = {};
let maxValue = 0;
let maxCount = 0;

for (let item of givenArray) {
  if (itemsMap[item] == null) {
    itemsMap[item] = 1;
  } else {
    itemsMap[item]++;
  }

  if (itemsMap[item] > maxCount) {
    maxValue = item;
    maxCount = itemsMap[item];
  }
}

console.log(`Value: ${maxValue}, Count: ${maxCount}`);
