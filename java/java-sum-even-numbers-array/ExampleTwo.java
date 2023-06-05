// https://codevscolor.com/java-sum-even-numbers-array
import java.util.Scanner;

public class ExampleTwo {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter the size of the array:");
            int size = sc.nextInt();

            int[] intArr = new int[size];

            System.out.println("Enter the elements of the array separated by space:");
            for (int i = 0; i < size; i++) {
                intArr[i] = sc.nextInt();
            }

            int sum = 0;
            int i = 0;

            while (i < size) {
                if (intArr[i] % 2 == 0) {
                    sum += intArr[i];
                }
                i++;
            }

            System.out.println("Sum of all even numbers in the array is: " + sum);
        }
    }
}