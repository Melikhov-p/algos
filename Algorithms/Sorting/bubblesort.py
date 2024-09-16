def bubble_sort(arr: list[int]):
    pass_amount = len(arr) - 1

    for right_limit in range(pass_amount, 0, -1):
        for i in range(right_limit):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


if __name__ == "__main__":
    arr = [10, 3, 9, 2, 8, 1, 7, 4, 6, 5]
    print(bubble_sort(arr))
