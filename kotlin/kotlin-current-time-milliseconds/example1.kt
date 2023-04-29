import java.util.Calendar

fun main() {
    val calendar = Calendar.getInstance()
    println(calendar.timeInMillis)
    println(System.currentTimeMillis())
}