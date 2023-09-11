// https://codevscolor.com/javascript-iterate-array-of-objects

const arr = [{id: 1, name: 'Alex', age: 20}, {id: 2, name: 'Bob', age: 22}, {id: 3, name: 'Chandler', age: 21}];

arr.forEach((item, index)=> {
    console.log(`Item at index ${index}: `, item);
});