// https://codevscolor.com/typescript-any-to-string

function getStringValue(value: any): string {
  return value?.toString();
}

console.assert(getStringValue(19) === "19", "Test 1");
console.assert(getStringValue(19.489) === "19.489", "Test 2");
console.assert(getStringValue("hello") === "hello", "Test 3");
console.assert(getStringValue(true) === "true", "Test 4");
console.assert(getStringValue(undefined) === undefined, "Test 5");
console.assert(getStringValue(null) === undefined, "Test 6");
