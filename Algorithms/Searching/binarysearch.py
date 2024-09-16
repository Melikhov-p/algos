def binary_search(arr: list, target: int):
    """Обязательное условие: отсортированный массив"""
    left_limit = 0
    right_limit = len(arr) - 1
    found = False

    while left_limit <= right_limit and not found:
        mid = (left_limit + right_limit) // 2
        if arr[mid] == target:
            found = True
        else:
            if arr[mid] < target:
                right_limit = mid - 1
            else:
                left_limit = mid + 1

    return found


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr, 5))
