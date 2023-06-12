// https://codevscolor.com/dart-remove-last-string-character

import 'dart:io';

main() {
  print("Enter a string : ");
  var userInput = stdin.readLineSync();

  if (userInput != null) {
    print(userInput.substring(0, userInput.length - 1));
  }
}
