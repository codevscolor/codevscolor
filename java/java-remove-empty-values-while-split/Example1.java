// https://codevscolor.com/java-remove-empty-values-while-split

import java.util.Arrays;

public class Example1 {
    public static void main(String[] args) {
        String givenString = "one,two,,three,,four,,  , ,";

        String[] resultArray = Arrays.stream(givenString.split(",")).filter(e -> e.trim().length() > 0)
                .toArray(String[]::new);

        System.out.println(Arrays.toString(resultArray));
    }
}