    import java.util.*
    fun main(args: Array) {
        val intArray = intArrayOf(1, 2, 3, 4, 5)
        val charArray = charArrayOf('a', 'b', 'c', 'd', 'e')
        val floatArray = floatArrayOf(1.0f, 2.0f, 3.0f)
        println("First 3 values of ${Arrays.toString(intArray)} are ${intArray.take(3)}")
        println("First 2 values of ${Arrays.toString(charArray)} are ${charArray.take(2)}")
        println("First 5 values of ${java.util.Arrays.toString(floatArray)} are ${floatArray.take(5)}")
    }
