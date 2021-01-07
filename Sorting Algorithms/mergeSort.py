def solve(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        solve(L)
        solve(R)
        merge(arr, L, R)

    return arr


def merge(arr, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            k += 1
            i += 1
        elif L[i] > R[j]:
            arr[k] = R[j]
            k += 1
            j += 1

    while i < len(L):
        arr[k] = L[i]
        k += 1
        i += 1

    while j < len(R):
        arr[k] = R[j]
        k += 1
        j += 1

    return arr


arr = [22, 2, 19, 15, 10, 11, 1]
result = solve(arr)
print(result)
