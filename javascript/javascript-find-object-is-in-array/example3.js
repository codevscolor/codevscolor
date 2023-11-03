// https://codevscolor.com/javascript-find-object-is-in-array

let iframe = document.createElement('iframe');
document.body.appendChild(iframe);
iframeArray = window.frames[window.frames.length - 1].Array;

let arr = new iframeArray(1, 2, 3);

console.log(arr instanceof Array);  // false    
console.log(Array.isArray(arr));  // true