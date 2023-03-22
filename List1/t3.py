import math

A = []
B = []


def scalarProduct(A, B):
    scalar = 0
    for i in range(0, len(A)):
        scalar += A[i] * B[i]
    return scalar


def length(X):
    x = 0
    for i in range(0, len(X)):
        x += X[i] * X[i]
    return math.sqrt(x)


while True:
    while True:
        try:
            a = float(
                input("Type a coordinate to A vector (or any letter to exit): "))
        except ValueError:
            break
        else:
            A.append(a)
            print(A)

    while True:
        try:
            b = float(
                input("Type a coordinate to B vector (or any letter to exit): "))
        except ValueError:
            break
        else:
            B.append(b)
            print(B)
    if len(A) == len(B):
        break
    else:
        print("The dimensions of the vectors must be equal! Try again.")
        A.clear()
        B.clear()
        continue

cos = scalarProduct(A, B)/(length(A)*length(B))

print(f"Cosine of the angle between A and B is equal: {cos}")
