// https://codevscolor.com/kotlin-add-items-to-list
fun main() {
    val givenList = mutableListOf("one", "two", "three")
    givenList.add("four")

    println(givenList)

    givenList.add(0, "zero")
    println(givenList)
}