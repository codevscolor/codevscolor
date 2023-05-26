// https://codevscolor.com/4-different-ways-sort-string-characters-alphabetically-in-java

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class ThirdExample {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Enter a string:");
            String userInput = scanner.nextLine();

            Character[] charArray = new Character[userInput.length()];

            for (int i = 0; i < userInput.length(); i++) {
                charArray[i] = userInput.charAt(i);
            }

            Arrays.sort(charArray, Comparator.comparingInt(Character::toLowerCase));

            StringBuilder sb = new StringBuilder(charArray.length);
            for (Character c : charArray)
                sb.append(c.charValue());

            System.out.println("Sorted string: " + sb.toString());
        }
    }
}