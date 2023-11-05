// https://codevscolor.com/kotlin-sort-map-by-value
fun main() {
    val givenMap = hashMapOf<String, Int>()
    givenMap["one"] = 1
    givenMap["two"] = 2
    givenMap["three"] = 3
    givenMap["four"] = 4
    givenMap["five"] = 5
    givenMap["six"] = 6

    println("Given map :")
    givenMap.forEach { (k, v) -> println("$k => $v") }

    var sortedMap: MutableMap<String,Int> = LinkedHashMap()

    givenMap.entries.sortedBy { it.value }.forEach{sortedMap[it.key] = it.value}

    println("Sorted map :")
    sortedMap.forEach { (k, v) -> println("$k => $v") }
}