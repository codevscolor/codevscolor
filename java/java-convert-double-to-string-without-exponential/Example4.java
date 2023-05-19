// https://codevscolor.com/java-convert-double-to-string-without-exponential
import java.text.DecimalFormat;

public class Example4 {
    public static void main(String[] args) {
        double number = 12.000047823458;

        String pattern = "##.############";
        DecimalFormat decimalFormat = new DecimalFormat(pattern);

        System.out.println(decimalFormat.format(number));
    }
}