# similar(?)
def selection_sort(arr):
    # time complexity: O(n^2)
    # space complexity: O(1)
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]


# arr = [3, 1, 5, 4, 2]
# 3
# arr = [2, 1, 3, 4, 5]
# arr = [2, 1]
# arr = [4, 5]
def quick_sort(arr):
    medium = arr[0]
    lower_cnt = 0
    for i in range(len(arr)):
        if arr[i] < medium:
            lower_cnt += 1

    medium_idx = lower_cnt
    # swap
    arr[0], arr[medium_idx] = arr[medium_idx], arr[0]

    larger_idx = medium_idx + 1
    for i in range(medium_idx):
        if arr[i] > medium:
            while arr[larger_idx] > medium:
                larger_idx += 1
            arr[i], arr[larger_idx] = arr[larger_idx], arr[i]

    return quick_sort(arr[0:medium_idx]) + [medium] + quick_sort(arr[medium_idx + 1:])


# version 2
# arr = [2, 1]
# choose 2 as medium
# arr = [1, 2]
# quick_sort2([1])
# quick_sort2([])
#
# Time complexity: O(n * log(n))
# Space complexity: O(logN)
def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    medium = arr[0]
    lower_cnt = 0
    for i in range(len(arr)):
        if arr[i] < medium:
            lower_cnt += 1

    medium_idx = lower_cnt
    # swap
    arr[0], arr[medium_idx] = arr[medium_idx], arr[0]

    larger_idx = medium_idx + 1
    for i in range(medium_idx):
        if arr[i] > medium:
            while arr[larger_idx] > medium:
                larger_idx += 1
            arr[i], arr[larger_idx] = arr[larger_idx], arr[i]

    return quick_sort2(arr[0:medium_idx]) + [medium] + quick_sort2(arr[medium_idx + 1:])


# Time complexity: O(n * log(n))
# Space complexity: O(1)
def quick_sort3(arr, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr)

    if right - left <= 1:
        return arr

    medium = arr[left]
    lower_cnt = 0
    for i in range(left, right):
        if arr[i] < medium:
            lower_cnt += 1

    medium_idx = lower_cnt + left
    # swap
    arr[left], arr[medium_idx] = arr[medium_idx], arr[left]

    larger_idx = medium_idx + 1
    for i in range(left, medium_idx):
        if arr[i] > medium:
            while arr[larger_idx] > medium:
                larger_idx += 1
            arr[i], arr[larger_idx] = arr[larger_idx], arr[i]

    quick_sort3(arr, left, medium_idx)
    quick_sort3(arr, medium_idx + 1, right)
    return arr
