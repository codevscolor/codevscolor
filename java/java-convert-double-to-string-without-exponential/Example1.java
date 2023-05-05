// https://codevscolor.com/java-convert-double-to-string-without-exponential
public class Example1 {
    public static void main(String[] args) {
        double number = 12.000047823458;

        System.out.println(String.format("%f", number));
        System.out.println(String.format("%.0f", number));
        System.out.println(String.format("%.12f", number));
    }
}