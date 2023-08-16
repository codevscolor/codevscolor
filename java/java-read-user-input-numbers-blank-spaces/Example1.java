// https://codevscolor.com/java-read-user-input-numbers-blank-spaces

import java.util.Arrays;
import java.util.Scanner;

public class Example1 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Please enter three numbers with space:");

            int[] intArray = new int[3];
            for (int i = 0; i < 3; i++) {
                intArray[i] = scanner.nextInt();
            }

            System.out.println("You have entered: " + Arrays.toString(intArray));
        }
    }
}