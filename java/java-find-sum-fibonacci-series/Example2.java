// https://codevscolor.com/java-find-sum-fibonacci-series

import java.util.Scanner;

class Example2 {

    private static int findSum(int n) {
        int currentValue = 1, prevValue = 0, sum = 0, temp;

        if (n <= 0)
            return 0;

        if (n == 1)
            return 1;

        sum = 1;
        int i = 2;
        while (i < n) {
            temp = currentValue;
            currentValue = prevValue + currentValue;
            prevValue = temp;

            sum += currentValue;
            i++;
        }
        return sum;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter the value of n: ");
            int n = sc.nextInt();

            System.out.println("Sum = " + findSum(n));
        }
    }
}