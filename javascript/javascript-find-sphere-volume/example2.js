// https://codevscolor.com/javascript-find-sphere-volume
let radius = parseInt(prompt("Enter the radius", "0"), 0);
let volume = (4/3)* Math.PI * Math.pow(radius, 3);

console.log('Volume of Sphere: '+volume.toFixed(2));