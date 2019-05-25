import java.util.Vector;
public class Example {
    public static void main(String[] args) {
        Vector<string> strVector = new Vector<>();
        
        //1
        strVector.add(0,"one");
        strVector.add(1,"two");
        strVector.add(2,"three");
        //2
        System.out.println(strVector);
        
        //3
        strVector.add(1,"four");
        //4
        System.out.println(strVector);
    }
}
