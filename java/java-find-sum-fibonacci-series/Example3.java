// https://codevscolor.com/java-find-sum-fibonacci-series

import java.util.Scanner;

class Example3 {

    private static int findSum(int currentValue, int prevValue, int i, int n) {
        if (n <= 0)
            return 0;
        if (n == 1)
            return 1;

        if (i == n)
            return 0;

        return currentValue + findSum(currentValue + prevValue, currentValue, i + 1, n);
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter the value of n: ");
            int n = sc.nextInt();

            System.out.println("Sum = " + findSum(1, 0, 1, n));
        }

    }
}