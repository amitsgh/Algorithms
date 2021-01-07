def solve(arr, low, high):
  middle = (high + low)//2
  pivot = arr[middle]
  if low < high:
    p = partition(arr, pivot, low, high)
    solve(arr, low, p-1)
    solve(arr, p+1, high)
  return arr
  
def partition(a, pivot, i, j):
  while i < j:
    while a[i] < pivot:
      i+=1
    while a[j] > pivot:
      j-=1
    if i < j:
      a[i], a[j] = a[j], a[i]
  return j

arr = [22, 2, 19, 15, 10, 11, 1]
result = solve(arr, 0, len(arr)-1)
print(result)
