// https://codevscolor.com/kotlin-add-items-to-list
fun main() {
    val givenList = mutableListOf("one", "two", "three")
    givenList.plusAssign("four")
    givenList.plusAssign("five")
    givenList.plusAssign(arrayOf("six", "seven", "eight"))

    println(givenList)
}