# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:47:46 2020

@author: FatMaus
"""
import random

# 堆:一种平衡二叉树，以max heap为例，数组实现

class MaxHeap():
    def __init__(self, CAP:int, size:int=0, Array:list=[]):
        '''
        使用数组实现堆
        '''
        self.CAP = CAP
        self.size = size
        self.Array = Array
        for i in range(CAP):
            self.Array.append(None)
    
    def getleftChildIndex(self, parentIndex:int):
        '''
        左子节点索引，根据数组中平衡二叉树的定义获得
        '''
        return 2 * parentIndex + 1
    
    def getRightChildIndex(self, parentIndex:int):
        '''
        右子节点索引，根据数组中平衡二叉树的定义获得
        '''
        return 2 * parentIndex + 2
    
    def getParentIndex(self, childIndex:int):
        '''
        父节点索引，根据数组中平衡二叉树的定义获得
        '''
        return (childIndex - 1) // 2
    
    def hasLeftChild(self, index:int):
        '''
        判断是否存在左子节点
        '''
        return self.getleftChildIndex(index) < self.size
    
    def hasRightChild(self, index:int):
        '''
        判断是否存在右子节点
        '''
        return self.getRightChildIndex(index) < self.size
    
    def hasParent(self, index:int):
        '''
        判断是否存在父节点
        '''
        return self.getParentIndex(index) >= 0

    def leftChild(self, parentIndex:int):
        '''
        获取左子节点的值
        '''
        return self.Array[self.getleftChildIndex(parentIndex)]
    
    def rightChild(self, parentIndex:int):
        '''
        获取右子节点的值
        '''
        return self.Array[self.getRightChildIndex(parentIndex)]
    
    def parent(self, childIndex:int):
        '''
        获取父节点的值
        '''
        return self.Array[self.getParentIndex(childIndex)]
    
    def insert(self, elem:int):
        '''
        加入新元素，并放到合适的位置
        '''
        # 查看数组是否已满，若满则扩容
        if self.size == self.CAP:
            for i in range(self.CAP):
                self.Array.append(None)
            self.CAP *= 2
        # 将新元素放在末位
        self.Array[self.size] = elem
        self.size += 1
        # 开启末位判断机制
        self.heapifyUp()
        
    def heapifyUp(self):
        '''
        末位判断机制，若末位比父节点大，则与父节点交换位置
        不断迭代到比父节点小为止
        '''
        index = self.size - 1
        # 在满足条件前不断循环
        while self.hasParent(index) and self.parent(index) < self.Array[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)
            
    def swap(self, index1:int, index2:int):
        '''
        交换元素的位置
        '''
        self.Array[index1], self.Array[index2] = self.Array[index2], self.Array[index1]
    
    def poll(self):
        '''
        移除根节点，并设定新的根节点
        '''
        # 判断堆是否为空，空则报错
        if self.size == 0:
            print("heap is empty")
        # 删除并将末位节点填入根节点
        elem = self.Array[0]
        self.Array[0] = self.Array[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return elem
    
    def heapifyDown(self):
        '''
        首位判断机制，此节点比子节点小，则与最大的子节点交换位置
        不断迭代到比所有子节点大为止
        '''
        index = 0
        while self.hasLeftChild(index):
            largerChildIndex = self.getleftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) > self.leftChild(index):
                largerChildIndex = self.getRightChildIndex(index)
            if self.Array[index] < self.Array[largerChildIndex]:
                self.swap(index, largerChildIndex)
            else:
                break
            index = largerChildIndex
    
    def peek(self):
        '''
        查看根节点
        '''
        if self.size == 0:
            print("heap is empty")
        return self.Array[0]

# 简易测试
mh = MaxHeap(10)
for i in range(10):
    mh.insert(random.randint(1, 100))
print(mh.Array)
mh.poll()
print(mh.Array)