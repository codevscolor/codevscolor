// https://codevscolor.com/4-different-ways-sort-string-characters-alphabetically-in-java

import java.util.Arrays;
import java.util.Scanner;

class SecondExample {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Enter a string:");
            String userInput = scanner.nextLine();

            char[] charArray = userInput.toCharArray();

            Arrays.sort(charArray);
            System.out.println("Sorted string: " + String.valueOf(charArray));
        }
    }
}