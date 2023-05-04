// https://codevscolor.com/dart-find-sum-list-elements
main() {
  var sum = 0;
  var given_list = [1, 2, 3, 4, 5];
  var i = 0;

  while (i < given_list.length) {
    sum += given_list[i];
    i++;
  }

  print("Sum: ${sum}");
}
