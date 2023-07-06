// https://codevscolor.com/dart-linkedhashmap-contains-key-value

import 'dart:collection';

void main() {
  final linkedHMap = LinkedHashMap.from(
      {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'});

  final key = 5;

  final isAvailable = linkedHMap.keys.any((element) => element == key);

  print('isAvailable: ${isAvailable}');
}
