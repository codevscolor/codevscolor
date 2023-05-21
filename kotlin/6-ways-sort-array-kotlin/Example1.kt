// https://codevscolor.com/6-ways-sort-array-kotlin
import java.util.*

fun main() {
    val students = arrayOf(10,9,23,12,5,2,4,1)
    println("Original array : ${Arrays.toString(students)}")

    students.sort()
    println("Sorted array : ${Arrays.toString(students)}")
}