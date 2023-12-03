// https://codevscolor.com/kotlin-add-items-to-list
fun main() {
    val givenList = mutableListOf("one", "two", "three")
    givenList.addAll(0,arrayListOf("-3", "-2", "-1", "0"))
    
    println(givenList)
}