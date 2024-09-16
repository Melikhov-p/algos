

def insertion_sort(arr: list[int]):
    for i in range(1, len(arr)):
        j = i - 1
        next_el = arr[i]
        while (arr[j] > next_el) and (j>=0):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = next_el

    return arr


if __name__ == '__main__':
    arr = [10, 3, 9, 2, 8, 1, 7, 4, 6, 5]
    print(insertion_sort(arr))
