// https://codevscolor.com/javascript-find-matches-array-objects

let studentArr = [{
    id: 1,
    name: 'Alex',
    age: 20
},
{
    id: 2,
    name: 'Bob',
    age: 18
},
{
    id: 3,
    name: 'Chandler',
    age: 19
},
{
    id: 4,
    name: 'Daisy',
    age: 16
},
{
    id: 5,
    name: 'Eva',
    age: 20
}];


let filterArray = studentArr.filter(item => item.id % 2 === 0);

console.log(filterArray);