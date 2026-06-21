def sorted_insert(arr, val):
    """
    向有序数组中插入一个值，保持数组有序（升序）。
    返回插入后的新数组。
    """
    arr.append(val)
    i = len(arr) - 1
    while i > 0 and arr[i - 1] > arr[i]:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        i -= 1
    return arr


if __name__ == "__main__":
    a = [1, 3, 5, 7, 9]
    print("原数组:", a)
    a = sorted_insert(a, 4)
    print("插入4后:", a)
    a = sorted_insert(a, 0)
    print("插入0后:", a)
    a = sorted_insert(a, 10)
    print("插入10后:", a)
