def merge(A, B):
    len_A, len_B = len(A), len(B)
    C = [0] * (len_A + len_B)

    i, j, k = 0, 0, 0

    while i < len_A and j < len_B:
        if int(A[i]) <= int(B[j]):
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1

    while i < len_A:
        C[k] = A[i]
        i += 1
        k += 1

    while j < len_B:
        C[k] = B[j]
        j += 1
        k += 1

    return C


n = input().split()
k = input().split()

result = merge(n, k)
print(*result)
