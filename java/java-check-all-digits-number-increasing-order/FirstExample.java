// https://codevscolor.com/java-check-all-digits-number-increasing-order
import java.util.Scanner;

class FirstExample {
    public static void main(String args[]) {

        // 1
        int num;
        boolean isIncreasing = true;

        // 2
        try (Scanner scanner = new Scanner(System.in)) {
            // 3
            System.out.println("Enter a number : ");
            num = scanner.nextInt();

            // 4
            int currentDigit = num % 10;
            num = num / 10;

            // 5
            while (num > 0) {
                // 6
                if (currentDigit <= num % 10) {
                    isIncreasing = false;
                    break;
                }

                currentDigit = num % 10;
                num = num / 10;
            }

            // 7
            if (!isIncreasing) {
                System.out.println("Digits are not in increasing order.");
            } else {
                System.out.println("Digits are in increasing order.");
            }
        }

    }
}