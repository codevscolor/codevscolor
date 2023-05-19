
// https://codevscolor.com/java-take-string-blank-spaces-input
import java.util.Scanner;

public class Example3 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in).useDelimiter("\n")) {
            String str;

            System.out.println("Enter a string: ");
            str = sc.next();

            System.out.println("You have entered: " + str);
        }
    }
}
