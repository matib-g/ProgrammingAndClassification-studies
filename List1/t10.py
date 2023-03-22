def decToBi(x):
    if x >= 1:
        decToBi(x // 2)
    print(x % 2, end='')


x = int(input("Type some decimal number: "))
decToBi(x)
