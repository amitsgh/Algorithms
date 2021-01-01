arr = [4, 3, 1, 6, 40, 8]
n = 6

for i in range(1, n):
    value = arr[i]
    idx = i-1
    while idx >= 0 and arr[idx] > value:
        arr[idx+1] = arr[idx]
        idx -= 1 
    arr[idx+1] = value
