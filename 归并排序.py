# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:26:35 2020

@author: Administrator
"""

# 归并排序，时间复杂O(NlogN)，空间复杂O(N)，运用分治法

import random

# 生成需要排序的数组列表(无重复数)
numList = []
for i in range(10):
    num = random.randint(1, 100)
    if num in numList:
        continue
    else:
        numList.append(num)
        
# 先切分，后合并，递归合并
def mergeSort(numList:list, start:int, end:int):
    # 若只剩一个元素，则停止
    if end- start < 1:
        return
    middle = (start + end) // 2
    # 不断二分拆分，直至成为单个数字
    mergeSort(numList, start, middle)
    mergeSort(numList, middle + 1, end)
    # 先拆再排
    merge(numList, start, middle, end)
    
# 排序，中间数和左侧数比大小，边拆边比，比到最后完成
def merge(numList:list, left:int, mid:int, right:int):
    # 拷贝，保持原有样式以便后续操作
    helpList = numList.copy()
    leftStart = left
    rightStart = mid + 1
    for i in range(left, right+1):
        if leftStart > mid:
            # 此时元素仅剩一个，保证不溢出、不重复
            numList[i] = helpList[rightStart]
            rightStart += 1
        elif rightStart > right:
            # 此时元素仅一个，保证不溢出、不重复，作为奇数个数时的保险补充
            numList[i] = helpList[leftStart]
            leftStart += 1
        elif helpList[leftStart] < helpList[rightStart]:
            # 和else组成排序功能,中间加一的数和最左侧比大小
            numList[i] = helpList[leftStart]
            leftStart += 1
        else:
            numList[i] = helpList[rightStart]
            rightStart += 1
            
mergeSort(numList, 0, len(numList) - 1)
print(numList)