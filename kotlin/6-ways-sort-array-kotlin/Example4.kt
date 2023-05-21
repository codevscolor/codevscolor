// https://codevscolor.com/6-ways-sort-array-kotlin
import java.util.*

fun main() {
    val students = arrayOf(1,2,3,4,5,6,7,8,9,10)
    println("Original array: ${Arrays.toString(students)}")

    students.sortDescending(0, 5)
    println("Sorted array from index 0 to 5: ${Arrays.toString(students)}")
}