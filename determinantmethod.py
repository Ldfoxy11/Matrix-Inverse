def determinant(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    det = 0
    for j in range(n):
        minor = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(A[i][k])
            minor.append(row)
        sign = 1 if j % 2 == 0 else -1
        det += sign * A[0][j] * determinant(minor)
    return det


n = int(input())
A = []

for i in range(n):
    A.append(list(map(float, input().split())))

det = determinant(A)

if det == 0:
    print("Inverse does not exist.")
else:
    inverse = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            minor = []
            for r in range(n):
                if r == i:
                    continue
                row = []
                for c in range(n):
                    if c != j:
                        row.append(A[r][c])
                minor.append(row)

            sign = 1 if (i + j) % 2 == 0 else -1
            inverse[j][i] = sign * determinant(minor) / det

    for row in inverse:
        print(*row)