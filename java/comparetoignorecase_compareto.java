class Example{
    public static void main(String[] args){
        String str1 = "Hello";
        String str2 = "Hello";
        String str3 = "hello";
        String str4 = "mello";
        System.out.println(str1.compareToIgnoreCase(str2)+" "+str1.compareTo(str2));
        System.out.println(str1.compareToIgnoreCase(str3)+" "+str1.compareTo(str3));
        System.out.println(str1.compareToIgnoreCase(str4)+" "+str1.compareTo(str4));
        System.out.println(str3.compareToIgnoreCase(str4)+" "+str3.compareTo(str4));
    }
}
