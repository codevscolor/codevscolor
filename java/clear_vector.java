import java.util.Scanner;
import java.util.Vector;
public class Example {
    public static void main(String[] args) {
        //1
        Vector vector = new Vector<>();
        int size;
        Scanner sc = new Scanner(System.in);
        //2
        System.out.println("Enter the size of the vector : ");
        size = sc.nextInt();
        //3
        for (int i = 0; i < size; i++) {
            System.out.println("Enter value for position " + (i + 1) + " : ");
            vector.add(sc.nextInt());
        }
        //4
        System.out.println("You have entered : " + vector);
        System.out.println("Size of the vector is : " + vector.size());
        //5
        vector.clear();
        //6
        System.out.println("After the vector is cleared : " + vector);
        System.out.println("Size of the vector after cleared : " + vector.size());
    }
}
