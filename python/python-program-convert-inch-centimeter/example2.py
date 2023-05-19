# https://codevscolor.com/python-program-convert-inch-centimeter

def inch_to_cm(inch):
    return inch * 2.54

if __name__ == "__main__":
    inch_value = int(input('Enter the value in inch: '))

    print(f'{inch_value}″ = {inch_to_cm(inch_value)}cm')