// https://codevscolor.com/kotlin-5-ways-sort-list-ascending-descending

fun main() {
    val students = listOf(
        Student("Alex", 54), Student("Rob", 34),
        Student("Chandler", 11), Student("Bryan", 90)
    )

    println("Sorting using a comparator : ")
    val sortedStudents = students.sortedWith { student1, student2 -> student1.name.length - student2.name.length }
    sortedStudents.forEach { s -> println(s.name) }
}

class Student(val name: String, marks: Int)