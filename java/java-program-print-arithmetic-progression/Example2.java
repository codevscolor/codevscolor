// https://codevscolor.com/java-program-print-arithmetic-progression

import java.util.Scanner;

class Example2 {
    static void printAP(int a, int d, int n) {
        int currentValue = a;
        for (int i = 1; i <= n; i++) {
            System.out.print(currentValue + " ");
            currentValue += d;
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