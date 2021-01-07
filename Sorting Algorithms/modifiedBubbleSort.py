def solve(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                flag = True
        if not flag:
            return arr
            break

    return arr


arr = [22, 2, 19, 15, 10, 11, 1]
result = solve(arr)
print(result)
