import random
import sys

sys.setrecursionlimit(10000)


# ========== 1. 随机轴快速排序 ==========

def _partition(arr, lo, hi):
    """Lomuto 分区：随机选轴，避免最坏 O(n²)"""
    pivot_idx = random.randint(lo, hi)
    arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]

    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def _quick_sort(arr, lo, hi):
    if lo < hi:
        p = _partition(arr, lo, hi)
        _quick_sort(arr, lo, p - 1)
        _quick_sort(arr, p + 1, hi)


def quick_sort(arr: list):
    """随机轴快速排序（in-place）"""
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


# ========== 2. 三路快速排序 ==========

def _quick_sort_3way(arr, lo, hi):
    """三路分区：处理大量重复元素时避免退化"""
    if lo >= hi:
        return

    # 随机选轴
    pivot_idx = random.randint(lo, hi)
    arr[lo], arr[pivot_idx] = arr[pivot_idx], arr[lo]
    pivot = arr[lo]

    lt = lo       # arr[lo+1..lt] < pivot
    i = lo + 1    # arr[lt+1..i-1] == pivot
    gt = hi       # arr[gt..hi] > pivot

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1

    # arr[lo..lt-1] < pivot, arr[lt..gt] == pivot, arr[gt+1..hi] > pivot
    _quick_sort_3way(arr, lo, lt - 1)
    _quick_sort_3way(arr, gt + 1, hi)


def quick_sort_3way(arr: list):
    """三路快速排序（in-place），对大量重复元素高效"""
    _quick_sort_3way(arr, 0, len(arr) - 1)
    return arr


# ========== 测试 ==========
if __name__ == "__main__":
    # 测试随机轴快排
    a = [3, 6, 8, 10, 1, 2, 1]
    print("随机轴快排:", quick_sort(a.copy()))

    # 测试三路快排
    print("三路快排:  ", quick_sort_3way(a.copy()))

    # 大量重复元素对比
    many_dups = [2] * 1000 + [1] * 1000 + [3] * 1000
    random.shuffle(many_dups)

    import time

    t0 = time.time()
    quick_sort(many_dups.copy())
    print(f"\n大量重复元素(3000个,3种值):")
    print(f"  随机轴快排: {time.time() - t0:.4f}s")

    t0 = time.time()
    quick_sort_3way(many_dups.copy())
    print(f"  三路快排:   {time.time() - t0:.4f}s")

    # 已排序数组（测试随机轴防退化）
    sorted_arr = list(range(5000))
    t0 = time.time()
    quick_sort(sorted_arr.copy())
    print(f"\n已排序数组(5000个):")
    print(f"  随机轴快排: {time.time() - t0:.4f}s")

    t0 = time.time()
    quick_sort_3way(sorted_arr.copy())
    print(f"  三路快排:   {time.time() - t0:.4f}s")
