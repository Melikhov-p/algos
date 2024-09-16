def merge_sort(arr: list):
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = arr[mid:]
        right_half = arr[:mid]

        merge_sort(left_half)
        merge_sort(right_half)

        a, b, c = 0, 0, 0

        while a < len(left_half) and b < len(right_half):
            if left_half[a] < right_half[b]:
                arr[c] = left_half[a]
                a += 1
            else:
                arr[c] = right_half[b]
                b += 1
            c += 1

        while a < len(left_half):
            arr[c] = left_half[a]
            a += 1
            c += 1

        while b < len(right_half):
            arr[c] = right_half[b]
            b += 1
            c += 1

    return arr


if __name__ == '__main__':
    arr = [10, 3, 9, 2, 8, 1, 7, 4, 6, 5]
    print(merge_sort(arr))