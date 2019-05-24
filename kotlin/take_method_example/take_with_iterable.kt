    fun main(args: Array) {
        val list = listOf(1,2,3,4,5)
        val set = setOf(1,2,2,4,5,6)
        println("First 3 values of $list are ${list.take(3)}")
        println("First 7 values of $set are ${set.take(7)}")
    }
