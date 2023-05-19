
// https://codevscolor.com/java-take-string-blank-spaces-input
import java.util.Scanner;

public class Example1 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            String str;

            System.out.println("Enter a string: ");
            str = sc.nextLine();

            System.out.println("You have entered: " + str);
        }
    }
}
