def insertionSort1(n, arr):
    # Write your code here
    for i in range((n-1),0,-1):
        if arr[i] < arr[i-1]:
            tmp = arr[i]
            arr[i] = arr[i-1]
            print(*arr)
            arr[i-1] = tmp
    print(*arr)
