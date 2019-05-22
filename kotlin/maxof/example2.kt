data class Student(val age: Int) : Comparable {
    override fun compareTo(other: Student) = other.age - age
}
fun main(args: Array) {
    println("Byte comparision ${maxOf(1.toByte(), 2.toByte(), 3.toByte())}")
    println("Short comparision ${maxOf(1.toShort(), 2.toShort(), 3.toShort())}")
    println("Integer comparision ${maxOf(1, 2, 3)}")
    println("Long comparision ${maxOf(1L, 2L, 3L)}")
    println("Float comparision ${maxOf(1.2f, 2.4f, 3.4f)}")
    println("Double comparision ${maxOf(1.34, 2.44, 3.65)}")
    val student1 = Student(12)
    val student2 = Student(22)
    val student3 = Student(32)
    println(maxOf(student1, student2, student3))
    println(maxOf(student1, student2, student3, compareBy { it.age }))
}
