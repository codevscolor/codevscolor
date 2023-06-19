// https://codevscolor.com/java-program-print-arithmetic-progression

import java.util.Scanner;

class Example1 {
    static void printAP(int a, int d, int n) {
        for (int i = 1; i <= n; i++) {
            System.out.print(a + (i - 1) * d + " ");
        }
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int a, d, n;
            System.out.println("Enter the values of a, d and n: ");
            a = sc.nextInt();
            d = sc.nextInt();
            n = sc.nextInt();

            printAP(a, d, n);
        }
    }
}