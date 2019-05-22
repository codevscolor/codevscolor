data class Student(val age: Int) : Comparable {
    override fun compareTo(other: Student) = other.age - age
}
fun main(args: Array) {
    //1
    println("Byte comparision ${maxOf(1.toByte(), 2.toByte())}")
    println("Short comparision ${maxOf(1.toShort(), 2.toShort())}")
    println("Integer comparision ${maxOf(1, 2)}")
    println("Long comparision ${maxOf(1L, 2L)}")
    println("Float comparision ${maxOf(1.2f, 2.4f)}")
    println("Double comparision ${maxOf(1.34, 2.44)}")
    //2
    val student1 = Student(12)
    val student2 = Student(22)
    //3
    println(maxOf(student1, student2))
    println(maxOf(student1, student2, compareBy { it.age }))
}
