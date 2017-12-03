while True:
    try:
        a = int(input("Please enter positive integer: "))
        if a < 1 or a > 2 ** 31 - 1:
            raise ValueError
        break
    except ValueError:
        print("This input doesn't look like positive integer, try again.")

def findComplement(a):
    b=int((bin(a)[2:]).replace('1', '2').replace('0', '1').replace('2', '0'), 2)
    return b
print (findComplement(a))
