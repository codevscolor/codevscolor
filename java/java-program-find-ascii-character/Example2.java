// https://codevscolor.com/java-program-find-ascii-character

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter a character: ");

            char c = sc.next().charAt(0);

            System.out.println("Ascii : " + (int) c);
        }

    }
}