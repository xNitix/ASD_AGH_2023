from zad2testy import runtests

def binary_search(arr, val, fn):
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if fn(val, arr[mid_idx]):
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return left_idx  # It will never exceed the left side of an array


def longest_seq(arr, fn=lambda a, b: a > b):
    if len(arr) < 2: return len(arr)

    n = len(arr)
    top = []

    for i in range(n):
        j = binary_search(top, arr[i], fn)
        if j == len(top):
            top.append(arr[i])
        else:
            top[j] = arr[i]

    return top


def tower(A: 'array of bricks spans'):
    A = longest_seq(A, lambda curr, prev: curr[0] >= prev[0])
    A = longest_seq(A, lambda curr, prev: curr[1] <= prev[1])
    return len(A)

runtests( tower )
