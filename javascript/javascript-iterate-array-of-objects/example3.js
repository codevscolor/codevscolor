// https://codevscolor.com/javascript-iterate-array-of-objects

const arr = [{ id: 1, name: 'Alex', age: 20 }, { id: 2, name: 'Bob', age: 22 }, { id: 3, name: 'Chandler', age: 21 }];

let i = 0;

do {
    console.log(arr[i]);
    i++;
}while(i < arr.length);