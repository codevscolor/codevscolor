const number = parseInt(prompt("Enter a number : "));
let i = 1;

do {
  console.log(number + "*" + i + "=" + number * i);
  i++;
}while (i <= 10);
