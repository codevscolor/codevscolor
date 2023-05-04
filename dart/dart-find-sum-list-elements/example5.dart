// https://codevscolor.com/dart-find-sum-list-elements
main() {
  var sum = 0;
  var given_list = [1, 2, 3, 4, 5];

  sum = given_list.fold(0, (previous, current) => previous + current);

  print("Sum: ${sum}");
}
