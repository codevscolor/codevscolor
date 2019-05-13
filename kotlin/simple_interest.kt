import java.util.Scanner
fun main(args: Array<string>) {
    //1
    val scanner = Scanner(System.`in`)
    //2
    print("Enter principal amount : ")
    var p:Int = scanner.nextInt()
    //3
    print("Enter rate of interest : ")
    var r:Int = scanner.nextInt()
    //4
    print("Enter number of years : ")
    var n:Int = scanner.nextInt()
    //5
    var SI:Int = (p*n*r)/100
    //6
    println("Simple interest : "+SI)
}
