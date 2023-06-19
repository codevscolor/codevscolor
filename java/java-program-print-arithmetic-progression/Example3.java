// https://codevscolor.com/java-program-print-arithmetic-progression

import java.util.Scanner;

class Example3 {
    static void printAP(int d, int n, int current) {
        System.out.print(current + " ");

        if (n == 0)
            return;

        printAP(d, n - 1, current + d);
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int a, d, n;

            System.out.println("Enter the values of a, d and n: ");
            a = sc.nextInt();
            d = sc.nextInt();
            n = sc.nextInt();

            printAP(d, n - 1, a);
        }

    }
}