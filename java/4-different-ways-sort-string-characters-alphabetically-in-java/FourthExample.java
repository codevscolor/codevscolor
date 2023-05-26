// https://codevscolor.com/4-different-ways-sort-string-characters-alphabetically-in-java

import java.util.Comparator;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class FourthExample {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Enter a string:");
            String userInput = scanner.nextLine();

            String finalString = Stream.of(userInput.split(""))
                    .sorted(Comparator.comparingInt(o -> Character.toLowerCase(o.charAt(0))))
                    .collect(Collectors.joining());

            System.out.println("Sorted string: " + finalString);
        }
    }
}