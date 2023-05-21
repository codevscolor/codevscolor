// https://codevscolor.com/6-ways-sort-array-kotlin
fun main() {
    val students = arrayOf(Student("Alex", 5), Student("Bob", 2), Student("Harry", 1))

    println("Original array:")
    students.forEach { println(it) }

    students.sortBy { student -> student.rank}

    println("Final array:")
    students.forEach { println(it) }
}

data class Student(val name: String, val rank: Int)