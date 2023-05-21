// https://codevscolor.com/6-ways-sort-array-kotlin
import java.util.*

fun main() {
    val students = arrayOf(1,5,7,8,2,3,9,10)
    println("Original array: ${Arrays.toString(students)}")

    students.sortDescending()
    println("Sorted array: ${Arrays.toString(students)}")
}