// https://codevscolor.com/java-check-all-digits-number-increasing-order
import java.util.Scanner;

class ThirdExample {
    public static boolean isDigitsAscending(int num) {
        String numString = String.valueOf(num);

        for (int i = 0; i < numString.length() - 1; i++) {
            if (numString.charAt(i) > numString.charAt(i + 1)) return false;
        }

        return true;
    }

    public static void main(String args[]) {
        int num;

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Enter a number : ");
            num = scanner.nextInt();

            if (isDigitsAscending(num)) {
                System.out.println("Digits are in increasing order.");
            } else {
                System.out.println("Digits are not in increasing order.");
            }
        }

    }
}