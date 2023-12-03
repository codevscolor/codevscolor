// https://codevscolor.com/kotlin-add-items-to-list
fun main() {
    val givenList = mutableListOf("one", "two", "three")
    val newList = givenList.plus("four").plus("five").plus(arrayOf("six", "seven", "eight"))

    println(newList)

    val anotherList = givenList.plusElement("nine")
    println(anotherList)
}