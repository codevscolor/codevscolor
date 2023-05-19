// https://codevscolor.com/java-program-to-calculate-discount-price

import java.util.Scanner;

class DiscountModel {
    int finalPrice;
    int discountPrice;

    public DiscountModel(int finalPrice, int discountPrice) {
        this.finalPrice = finalPrice;
        this.discountPrice = discountPrice;
    }
}

public class Example3 {

    static DiscountModel getDiscount(int price, int discount) {
        int discountPrice = (price * discount) / 100;
        int finalPrice = price - discountPrice;

        return new DiscountModel(finalPrice, discountPrice);
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

        DiscountModel result = getDiscount(price, discount);

        System.out.println("Discount price is: " + result.discountPrice);
        System.out.println("Final price is: " + result.finalPrice);
    }
}