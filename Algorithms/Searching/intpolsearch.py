def intpol_search(arr: list, target: int):
    left_limit = 0
    right_limit = len(arr) - 1
    found = False

    while left_limit <= right_limit and arr[left_limit] <= target <= arr[right_limit] and not found:
        mid = left_limit + (target - arr[left_limit]) * (right_limit - left_limit) // (
            arr[right_limit] - arr[left_limit]
        )
        if arr[mid] == target:
            found = True
        if arr[mid] < target:
            left_limit = mid + 1
    return found


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(intpol_search(arr, 1))
