// https://codevscolor.com/java-move-zeros-integer-array-start
class Main {
    public static void main(String args[]) {
        // 1
        int[] array = { 1, 2, 0, 4, 6, 0, 9, 0, 4, 0, 3, 0, 9, 0, 1, 0, 3, 0 };

        // 2
        int current = array.length - 1;

        // 3
        for (int i = array.length - 1; i >= 0; i--) {
            if (array[i] != 0) {
                array[current] = array[i];
                current--;
            }
        }

        // 4
        while (current >= 0) {
            array[current] = 0;
            current--;
        }

        // 5
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
    }
}