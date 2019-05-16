import java.util.Enumeration;
import java.util.Scanner;
import java.util.Vector;
public class Example {
    public static void main(String[] args) {
        //1
        int size;
        Vector<string> strVector = new Vector<>();
        Scanner sc = new Scanner(System.in);
        //2
        System.out.println("Enter the size of the vector : ");
        size = sc.nextInt();
        //3
        for (int i = 0; i < size; i++) {
            System.out.println("Enter a string value for position " + (i + 1) + " : ");
            strVector.add(sc.next());
        }
        //4
        System.out.println("You have entered : ");
        //5
        Enumeration<string> enumeration = strVector.elements();
        //6
        while(enumeration.hasMoreElements()){
            System.out.println(enumeration.nextElement());
        }
    }
}
