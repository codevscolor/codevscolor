// https://codevscolor.com/kotlin-5-ways-sort-list-ascending-descending

fun main() {
    val students = listOf(
        Student("Alex", 54), Student("Rob", 34),
        Student("Chandler", 11), Student("Bryan", 90)
    )

    println("Sorting by ascending : ")
    val sortedStudents = students.sortedBy { student -> student.name }
    sortedStudents.forEach { s -> println(s.name) }

    println("Sorting by descending : ")
    val dSortedStudents = sortedStudents.sortedByDescending { student -> student.name }
    dSortedStudents.forEach { s -> println(s.name) }
}

class Student(val name: String, marks: Int)