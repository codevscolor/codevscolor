// https://codevscolor.com/java-sort-integer-array-ascending
import java.util.Arrays;
import java.util.Scanner;

class SecondExample {
    public static void main(String[] args) {

        try (Scanner sc = new Scanner(System.in)) {

            System.out.println("Enter number of array elements:");
            int size = sc.nextInt();

            int[] numArray = new int[size];

            for (int i = 0; i < size; i++) {
                System.out.print("Enter element: ");
                numArray[i] = sc.nextInt();
            }

            System.out.println("You have entered: " + Arrays.toString(numArray));

            Arrays.sort(numArray);

            System.out.println("Final array after the sorting: " + Arrays.toString(numArray));
        }

    }
}