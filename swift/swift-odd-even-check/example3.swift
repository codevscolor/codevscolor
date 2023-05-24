// https://codevscolor.com/swift-odd-even-check

var arr:[Double] = [1,2,3,4,5,6]

for n in arr{
    if(n.remainder(dividingBy: 2) == 0){
        print("\(n) is even")
    }else{
        print("\(n) is odd")
    }
}