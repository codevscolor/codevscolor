// https://codevscolor.com/java-program-to-calculate-discount-price

import java.util.Scanner;

public class Example1 {

    public static void main(String[] args) {
        int price;
        int discount;

        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter price of the product:");
            price = sc.nextInt();

            System.out.println("Enter the discount(%) of the product:");
            discount = sc.nextInt();
        }

        int discountPrice = (price * discount) / 100;
        int finalPrice = price - discountPrice;

        System.out.println("Discount price is: " + discountPrice);
        System.out.println("Final price is: " + finalPrice);
    }
}