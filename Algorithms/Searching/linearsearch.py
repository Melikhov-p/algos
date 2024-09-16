from typing import Any


def linear_search(arr: list, target: Any):
    index = 0
    found = False
    while index < len(arr) and not found:
        if arr[index] == target:
            found = True
        else:
            index += 1
    return found


if __name__ == '__main__':
    arr = [10, 3, 9, 2, 8, 1, 7, 4, 6, 5]
    print(linear_search(arr, 12))
