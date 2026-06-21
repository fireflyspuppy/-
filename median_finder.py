# -*- coding: utf-8 -*-
import heapq


class MedianFinder:
    def __init__(self):
        self.maxHeap = []  # 大顶堆，存较小的一半（Python heapq 是小顶堆，值取负来模拟大顶堆）
        self.minHeap = []  # 小顶堆，存较大的一半

    def addNum(self, num):
        # 先插入 maxHeap，再把 maxHeap 的最大值移到 minHeap，保证 maxHeap <= minHeap
        heapq.heappush(self.maxHeap, -num)
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        # 保持平衡：maxHeap 大小 >= minHeap 大小
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self):
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        return (-self.maxHeap[0] + self.minHeap[0]) / 2.0


if __name__ == "__main__":
    # 测试 1: [1,2,3]
    print("=== 测试 1: 依次添加 1, 2, 3 ===")
    mf1 = MedianFinder()
    mf1.addNum(1)
    print("添加 1  -> 中位数: {}".format(mf1.findMedian()))   # 1
    mf1.addNum(2)
    print("添加 2  -> 中位数: {}".format(mf1.findMedian()))   # 1.5
    mf1.addNum(3)
    print("添加 3  -> 中位数: {}".format(mf1.findMedian()))   # 2

    # 测试 2: [5, 15, 1, 3]
    print("\n=== 测试 2: 依次添加 5, 15, 1, 3 ===")
    mf2 = MedianFinder()
    mf2.addNum(5)
    print("添加 5  -> 中位数: {}".format(mf2.findMedian()))   # 5
    mf2.addNum(15)
    print("添加 15 -> 中位数: {}".format(mf2.findMedian()))   # 10
    mf2.addNum(1)
    print("添加 1  -> 中位数: {}".format(mf2.findMedian()))   # 5
    mf2.addNum(3)
    print("添加 3  -> 中位数: {}".format(mf2.findMedian()))   # 4

    # 测试 3: 负数
    print("\n=== 测试 3: 负数 [-1, -2, -3] ===")
    mf3 = MedianFinder()
    mf3.addNum(-1)
    mf3.addNum(-2)
    mf3.addNum(-3)
    print("添加 -1, -2, -3 -> 中位数: {}".format(mf3.findMedian()))  # -2

    # 测试 4: 重复值
    print("\n=== 测试 4: 重复值 [2, 2, 2] ===")
    mf4 = MedianFinder()
    mf4.addNum(2)
    mf4.addNum(2)
    mf4.addNum(2)
    print("添加 2, 2, 2 -> 中位数: {}".format(mf4.findMedian()))  # 2
