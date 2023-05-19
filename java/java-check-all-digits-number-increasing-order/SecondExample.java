import java.util.Scanner;

class SecondExample {
    public static boolean isDigitsAscending(int num) {
        int currentDigit = num % 10;
        num = num / 10;

        while (num > 0) {
            if (currentDigit <= num % 10) {
                return false;
            }

            currentDigit = num % 10;
            num = num / 10;
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