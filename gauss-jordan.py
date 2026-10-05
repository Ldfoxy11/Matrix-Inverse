n = int(input())
A = []

for i in range(n):
    A.append(list(map(float, input().split())))

for i in range(n):
    A[i] += [1.0 if i == j else 0.0 for j in range(n)]

for i in range(n):
    if A[i][i] == 0:
        for k in range(i + 1, n):
            if A[k][i] != 0:
                A[i], A[k] = A[k], A[i]
                break
        else:
            print("Inverse does not exist.")
            exit()

    pivot = A[i][i]

    for j in range(2 * n):
        A[i][j] /= pivot

    for k in range(n):
        if k != i:
            factor = A[k][i]
            for j in range(2 * n):
                A[k][j] -= factor * A[i][j]

print("Inverse matrix:")

for i in range(n):
    print(*A[i][n:])