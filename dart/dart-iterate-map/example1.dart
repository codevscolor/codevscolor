// https://codevscolor.com/dart-iterate-map

main() {
  var numMap = Map();
  numMap["one"] = 1;
  numMap["two"] = 2;
  numMap["three"] = 3;
  numMap["four"] = 4;
  numMap["five"] = 5;

  numMap.forEach((k, v) => print("Key : $k, Value : $v"));
}