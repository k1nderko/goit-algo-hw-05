def binary_search_with_upper_bound(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = arr[-1]

    while low <= high:
        mid = (low + high) // 2
        iterations += 1
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            return iterations, arr[mid]

    return iterations, upper_bound


if __name__ == "__main__":
    arr = [1.1, 1.3, 2.5, 3.8, 4.6]
    print(binary_search_with_upper_bound(arr, 3.5))
    print(binary_search_with_upper_bound(arr, 4))
    print(binary_search_with_upper_bound(arr, 6.0))
    print(binary_search_with_upper_bound(arr, 2.5))
    print(binary_search_with_upper_bound(arr, 0))
