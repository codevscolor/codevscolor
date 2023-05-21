// https://codevscolor.com/6-ways-sort-array-kotlin
import java.util.*

fun main() {
    val students = arrayOf(10,9,8,7,6,5,4,3,2,1)
    println("Original array: ${Arrays.toString(students)}")

    students.sort(0,5)
    println("Sorted array from index 0 to 5: ${Arrays.toString(students)}")
}