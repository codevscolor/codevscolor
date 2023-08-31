// https://codevscolor.com/javascript-find-matches-array-objects

const studentFilter = (student) => student?.id % 2 === 2 && student?.age > 16;

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

let filterArray = studentArr.filter(studentFilter);

console.log(`filterArray: `,filterArray);
console.log(`studentArr: `, studentArr);