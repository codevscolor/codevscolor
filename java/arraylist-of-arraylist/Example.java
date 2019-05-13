import java.util.ArrayList;
import java.util.Scanner;

public class Example {
    public static void main(String[] args) {
        //1
        ArrayList<ArrayList> myList = new ArrayList<>();
        
        //2
        int arrayListCount, itemCount;
        Scanner scanner = new Scanner(System.in);
        
        //3
        System.out.println("Enter total number of ArrayList to add : ");
        arrayListCount = scanner.nextInt();
        
        //4
        System.out.println("Enter total values for each ArrayList : ");
        itemCount = scanner.nextInt();
        
        //5
        for (int i = 0; i < arrayListCount; i++) {
            //6
            System.out.println("Enter all values for ArrayList " + (i + 1) + " : ");
            ArrayList list = new ArrayList<>();
            //7
            for (int j = 0; j < itemCount; j++) {
                //8
                System.out.println("Enter value " + (j + 1) + " : ");
                list.add(scanner.next());
            }
            //9
            myList.add(list);
        }
        
        //10
        System.out.println(myList);
    }
}
