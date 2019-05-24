    public class Example {
        public static void main(String[] args) {
            //1
            String str1 = "Hello World";
            String str2 = "And hello Universe";
            String str3 = "Hello Again";
            //2
            System.out.println("Region matching 1 : " + str1.regionMatches(0, str2, 4, 5));
            //3
            System.out.println("Region matching 2 : " + str1.regionMatches(0, str3, 0, 5));
            //4
            System.out.println("Region matching 3 : " + str1.regionMatches(true, 0, str2, 4, 5));
            //5
            System.out.println("Region matching 4 : " + str1.regionMatches(false, 0, str2, 4, 5));
        }
    }
