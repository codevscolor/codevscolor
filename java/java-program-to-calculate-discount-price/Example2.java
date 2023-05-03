// https://codevscolor.com/java-program-to-calculate-discount-price

import java.util.Scanner;

public class Example2 {

    static int getDiscount(int price, int discount) {
        return (price * discount) / 100;
    }

    static int getFinalPrice(int price, int discountPrice) {
        return price - discountPrice;
    }

    public static void main(String[] args) {
        int price;
        int discount;

        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter price of the product :");
            price = sc.nextInt();

            System.out.println("Enter the discount(%) of the product :");
            discount = sc.nextInt();
        }

        int discountPrice = getDiscount(price, discount);
        int finalPrice = getFinalPrice(price, discountPrice);

        System.out.println("Discount price is: " + discountPrice);
        System.out.println("Final price is: " + finalPrice);
    }
}