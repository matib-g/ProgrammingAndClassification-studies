A = ['d', 4, 'g', 3, 'f', 1, 'p']
S = []
N = []

for i in range(0, len(A)):
    if isinstance(A[i], str) == True:
        S.append(A[i])
    elif isinstance(A[i], int) == True:
        N.append(A[i])
S.sort()
N.sort()
X = S + N

print(X)
