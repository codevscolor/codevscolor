// https://codevscolor.com/6-ways-sort-array-kotlin
fun main() {
    val students = arrayOf(5,2,6,9,10,1,44,23)
    println("Original array: ${students.contentToString()}")

    val sortedArray = students.sortedArray()
    println("Sorted array: ${sortedArray.contentToString()}")

    val descendingSortedArray = students.sortedArrayDescending()
    println("Sorted array in descending: ${descendingSortedArray.contentToString()}")
}