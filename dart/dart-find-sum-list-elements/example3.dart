// https://codevscolor.com/dart-find-sum-list-elements
main() {
  var sum = 0;
  var given_list = [1, 2, 3, 4, 5];

  given_list.forEach((e) => sum += e);

  print("Sum: ${sum}");
}
