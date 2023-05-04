// https://codevscolor.com/dart-find-sum-list-elements
main() {
  // method 1
  var sum = 0;
  var given_list = [1, 2, 3, 4, 5];
  for (var i = 0; i < given_list.length; i++) {
    sum += given_list[i];
  }

  print("Sum (for loop): ${sum}");

  // method 2
  var i = 0;
  sum = 0;
  while (i < given_list.length) {
    sum += given_list[i];
    i++;
  }

  print("Sum (while loop): ${sum}");

  // method 3
  sum = 0;
  given_list.forEach((e) => sum += e);
  print("Sum (forEach): ${sum}");

  // method 4
  sum = given_list.length > 0
      ? given_list.reduce((value, element) => value + element)
      : 0;
  print("Sum (reduce): ${sum}");

  // method 5
  sum = given_list.fold(0, (previous, current) => previous + current);
  print("Sum (fold): ${sum}");
}
