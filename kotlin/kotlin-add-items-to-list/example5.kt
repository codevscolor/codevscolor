// https://codevscolor.com/kotlin-add-items-to-list
fun main() {
    val givenList = mutableListOf("one", "two", "three")
    val newList = givenList + "four" + "five" + "six"

    println(newList)
}