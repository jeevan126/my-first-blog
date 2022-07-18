def fun(name):
    if name%2 == 0:
        print("even")
    else:
        print("odd")
    for i in range(9):
        print(i)


a = int(input())
fun(a)
