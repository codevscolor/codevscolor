// https://codevscolor.com/java-find-sum-fibonacci-series

import java.util.Scanner;

class Example1 {

    private static int findSum(int n) {
        // 3
        int currentValue = 1, prevValue = 0, temp;

        // 4
        if (n <= 0)
            return 0;

        if (n == 1)
            return 1;

        // 5
        int sum = 1;
        for (int i = 2; i < n; i++) {
            temp = currentValue;
            currentValue = prevValue + currentValue;
            prevValue = temp;

            sum += currentValue;
        }
        return sum;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            // 1
            int n;
            System.out.println("Enter the value of n: ");
            n = sc.nextInt();

            // 2
            System.out.println("Sum = " + findSum(n));
        }
    }
}