// https://codevscolor.com/java-sort-integer-array-ascending
import java.util.Arrays;

class FourthExample {
    public static void main(String[] args) {

        int[] numArray = { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 };

        System.out.println("You have entered: " + Arrays.toString(numArray));

        Arrays.parallelSort(numArray);

        System.out.println("Final array after the sorting: " + Arrays.toString(numArray));

    }
}