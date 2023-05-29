// https://codevscolor.com/react-native-detect-text-change

import { useState } from "react";
import { StyleSheet, Text, View, TextInput } from "react-native";

export default function App() {
  const [text, setText] = useState("");

  const changeText = (inputText) => {
    const formattedText = "\u{1F632}" + inputText;
    setText(formattedText);
  };

  const endEditing = () => {
    const formattedText = text + "\u{2708}";
    setText(formattedText);
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.textinput}
        placeholder="Enter your text here"
        onChangeText={changeText}
        onEndEditing={endEditing}
      />
      <Text style={styles.textView}>{text}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F5FCFF",
  },
  textinput: {
    fontSize: 30,
    textAlign: "center",
    marginTop: 60,
    marginRight: 20,
    marginLeft: 20,
    padding: 10,
    borderColor: "grey",
    borderWidth: 1,
    borderRadius: 5,
  },
  textView: {
    fontSize: 40,
    marginTop: 30,
    textAlign: "center",
  },
});
