# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:13:31 2020

@author: Administrator
"""

# 快速排序，平均时间复杂度O(NlogN)，运用了分治法，空间复杂O(N)

import random

# 生成需要排序的数组列表(无重复数)
numList = []
for i in range(10):
    num = random.randint(1, 100)
    if num in numList:
        continue
    else:
        numList.append(num)

# 运用分治法，快排递归
def quickSort(numList:list, left:int, right:int):
    if left >= right:
        return
    # 排列并获取切割点
    partitionIndex = partition(numList, left, right)
    # 二分递归
    quickSort(numList, left, partitionIndex - 1)
    quickSort(numList, partitionIndex + 1, right)

# 排列并返回交点
def partition(numList:list, left:int, right:int):
    # 选择一个元素作为基准元素
    pivot = numList[right]
    leftIndex = left
    rightIndex = right - 1
    while True:
        while leftIndex < right and numList[leftIndex] <= pivot:
            leftIndex += 1
        while rightIndex >= left and numList[rightIndex] > pivot:
            rightIndex -= 1
        # 左右并进，碰头则结束循环
        if leftIndex > rightIndex:
            break
        # 出现不符合条件的，交换位置
        swap(numList, leftIndex, rightIndex)
    # 基准元素归位，返回交点
    swap(numList, leftIndex, right)
    return leftIndex

# 元素交换
def swap(numList:list, left:int, right:int):
    numList[left], numList[right] = numList[right], numList[left]

quickSort(numList, 0, len(numList) - 1)
print(numList)