#python source code or python module
#sequential  execution


number= 10       #main thread


def show():
    global number
    number = 20
    print(">>1. number is :",number)
show()

print(">>2. number is :", number)      # it is in main thread

