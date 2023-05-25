// https://codevscolor.com/kotlin-5-ways-sort-list-ascending-descending

fun main() {
    val strList = listOf(
        "a", "abcde", "abc", "ab", "abcd", "abcdef"
    )

    println("Ascending order: ")
    val ascendingList = strList.sortedBy { it.length }
    ascendingList.forEach { s -> println(s) }

    println("Descending order: ")
    val descendingList = strList.sortedByDescending { it.length }
    descendingList.forEach { s -> println(s) }
}