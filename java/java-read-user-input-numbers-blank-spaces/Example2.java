
// https://codevscolor.com/java-read-user-input-numbers-blank-spaces
import java.util.Arrays;
import java.util.Scanner;

public class Example2 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Please enter the numbers separated with space:");

            String numString = scanner.nextLine();
            String[] nums = numString.split(" ");

            int[] intArray = new int[nums.length];

            for (int i = 0; i < nums.length; i++) {
                intArray[i] = Integer.parseInt(nums[i]);
            }

            System.out.println("You have entered: " + Arrays.toString(intArray));
        }
    }
}