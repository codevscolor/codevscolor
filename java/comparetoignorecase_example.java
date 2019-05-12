public class Example {
    public static void main(String[] args) {
        String str1 = "Hello World";
        String str2 = "Hello World";
        String str3 = "hello world";
        String str4 = "Aello world";
        //1
        System.out.println("Comparison 1 : "+str1.compareToIgnoreCase(str2));
        //2
        System.out.println("Comparison 2 : "+str1.compareToIgnoreCase(str3));
        //3
        System.out.println("Comparison 3 : "+str1.compareToIgnoreCase(str4));
        //4
        System.out.println("Comparison 4 : "+str3.compareToIgnoreCase(str4));
        //5
        System.out.println("Comparison 5 : "+str4.compareToIgnoreCase(str3));
    }
}
