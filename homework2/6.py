import re

a = input("Please enter your expression: ")
regex = re.compile("^[-]{0,1}[0-9]{1,6}[*|/|+/-]{1}[-]{0,1}[0-9]{1,6}[=]{1}[-]{0,1}[0-9]{1,10}$")
if not regex.match(a) or len(a) > 100:
    print("ERROR")
    exit()

def math(a):
    answer = ""
    fir = ""
    sec = ""
    res = ""
    operator = ""
    mylist = re.split("[=]", a)
    res = ''.join(mylist[1])
    tmp = ''.join(mylist[0])

    for i in range(len(tmp)):
        if tmp[i] == "+" or tmp[i] == "*" or tmp[i] == "/":
            fir = (tmp[0:i])
            sec = (tmp[i+1:len(tmp)])
            operator = tmp[i]
        elif tmp[i] == "-" and i != 0 and operator == "":
            fir = (tmp[0:i])
            sec = (tmp[i+1:len(tmp)])
            operator = tmp[i]
    if (abs(int(fir))) > 30000 or (abs(int(sec))) > 30000 or (abs(int(res))) > 30000:
        answer = "ERROR"
    elif operator == "+" and int(fir) + int(sec) == int(res):
        answer = "YES"
    elif operator == "-" and int(fir) - int(sec) == int(res):
        answer = "YES"
    elif operator == "*" and int(fir) * int(sec) == int(res):
        answer = "YES"
    elif operator == "/" and int(sec) != 0 and int(fir) / int(sec) == int(res) and int(fir) % int(sec) == 0:
        answer = "YES"
    else:
        answer = "NO"

    return (answer)

print(math(a))
