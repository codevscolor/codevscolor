// https://codevscolor.com/swift-odd-even-check

var arr = [1,2,3,4,5,6]

for n in arr{
    if(n.isMultiple(of: 2)){
        print("\(n) is even")
    }else{
        print("\(n) is odd")
    }
}