def bubble_sort(arr: list[int]):
    arr_length = len(arr)
    pass_amount = arr_length - 1

    for passNo in range(pass_amount):
        for i in range(passNo, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]

    return arr


if __name__ == "__main__":
    arr = [10, 3, 9, 2, 8, 1, 7, 4, 6, 5]
    print(bubble_sort(arr))

