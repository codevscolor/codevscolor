// https://codevscolor.com/java-convert-negative-to-positive

import java.util.Scanner;

public class ThirdExample {

    public static void main(String[] args) {
        double givenNumber;
        double positiveNumber;

        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter a number: ");

            givenNumber = sc.nextDouble();

            if (givenNumber < 0) {
                positiveNumber = Math.abs(givenNumber);
                System.out.println("Positive number: " + positiveNumber);
            } else {
                System.out.println("Please enter a negative number.");
            }
        }

    }
}