// https://codevscolor.com/java-move-zeros-integer-array-start
import java.util.Arrays;

public class Example {
    public static void main(String args[]) {
        int[] array = { 1, 2, 0, 4, 6, 0, 9, 0, 4, 0, 3, 0, 9, 0, 1, 0, 3, 0 };

        Arrays.sort(array);

        for (int j : array) {
            System.out.print(j + " ");
        }
    }
}