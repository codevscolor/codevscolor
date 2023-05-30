// https://codevscolor.com/java-sort-integer-array-ascending
import java.util.Arrays;
import java.util.Scanner;

class FirstExample {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int tempValue;

            System.out.println("Enter number of array elements:");
            int size = sc.nextInt();

            int[] numArray = new int[size];

            for (int i = 0; i < size; i++) {
                System.out.print("Enter element: ");
                numArray[i] = sc.nextInt();
            }

            System.out.println("You have entered: " + Arrays.toString(numArray));

            for (int i = 0; i < numArray.length; i++) {
                for (int j = i + 1; j < numArray.length; j++) {
                    if (numArray[i] > numArray[j]) {
                        tempValue = numArray[i];
                        numArray[i] = numArray[j];
                        numArray[j] = tempValue;
                    }
                }
            }

            System.out.println("Array after sorting: " + Arrays.toString(numArray));
        }

    }
}