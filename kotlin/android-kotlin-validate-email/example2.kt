// https://codevscolor.com/android-kotlin-validate-email

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log

class MainActivity : AppCompatActivity() {

    fun isValidString(str: String): Boolean{
        return android.util.Patterns.EMAIL_ADDRESS.matcher(str).matches()
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val emails = arrayOf("hello@gmail.com", "one.com")

        emails.forEach {
            Log.d("MainActivity","is valid email $it => ${isValidString(it)}")
        }
    }
}