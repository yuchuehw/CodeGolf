from string import ascii_uppercase, digits
import sys

S = digits + (_ := ascii_uppercase) + _.lower() + "-"


def infect(A, x, y, v):
    if x < 0 or y < 0 or x > 8 or y > 8:
        return
    if A[x][y] == "#":
        return
    if v > S.index(A[x][y]):
        return
    A[x][y] = S[v]
    infect(A, x - 1, y, v + 1)
    infect(A, x, y - 1, v + 1)
    infect(A, x + 1, y, v + 1)
    infect(A, x, y + 1, v + 1)


for arg in sys.argv[1:]:
    A = [[*_] for _ in arg.split()]
    for i in range(9):
        for j in range(9):
            if A[i][j] == "0":
                infect(A, i, j, 0)
    print("\n".join("".join(i)for i in A))
    print()
