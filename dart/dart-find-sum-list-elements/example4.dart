// https://codevscolor.com/dart-find-sum-list-elements
main() {
  var given_list = [1, 2, 3, 4, 5];

  var sum = given_list.length > 0
      ? given_list.reduce((value, element) => value + element)
      : 0;

  print("Sum: ${sum}");
}
