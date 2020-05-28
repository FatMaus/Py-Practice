# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:32:20 2020

@author: Administrator
"""

# 哈希表

class HashNode():
    def __init__(self, key:str, value:int, nextEle=None):
        '''
        哈希表节点，三个属性
        键值对key, value加上指向下一个的指针nextEle(哈希值冲突时用)
        '''
        self.key = key
        self.value = value
        self.nextEle = nextEle
        
class HashMap():
    def __init__(self, CAP:int=10, size:int=0):
        '''
        哈希表初始化，三个属性
        存储节点的列表Array，数组容量CAP
        哈希表元素总数size
        '''
        self.CAP = CAP
        self.Array = []
        self.size = size
        # 数组初始化，占住索引以便添加元素
        for i in range(self.CAP):
            self.Array.append(None)
    
    def getIndex(self, key:str):
        '''
        根据键获取哈希值，并求余得出节点在数组中的存储位
        '''
        hashCode = hash(key)
        index = hashCode % self.CAP
        return index
        
    def add(self, key:str, value:int):
        '''
        向哈希表添加元素，节点为空直接加入
        节点不为空则判断是否有同名键，有同名键则覆盖，无则增加键值对
        新增键值对作为链表的首位占据数组位置
        '''
        # 获取存储节点的位置
        ArrIndex = self.getIndex(key)
        # 查看此位置是否为空
        head = self.Array[ArrIndex]
        while head != None:
            # 查看是否有重复键
            if head.key == key:
                head.value = value
                return
            # 顺延查找，直到None
            head = head.nextEle
        # 非空链表且无重复键时，还原head初始值，再行添加元素
        head = self.Array[ArrIndex]
        newNode = HashNode(key, value, head)
        # 数组存储链表第一位即可
        self.Array[ArrIndex] = newNode
        self.size += 1
        # 存储过多时考虑扩容
        if self.size / self.CAP >= 0.8:
            self.expansion()
    
    def expansion(self):
        '''
        扩容函数，给内置数组扩容
        降低链表长度，以优化查找速度
        '''
        # 备份现有
        backup = self.Array
        # 建立扩容后的新容器
        self.Array = []
        self.CAP *= 2
        self.size = 0
        # 初始化新容器后装入备份
        for i in range(self.CAP):
            self.Array.append(None)
        for node in backup:
            while node != None:
                self.add(node.key, node.value)
                node = node.nextEle
    
    def get(self, key:str):
        '''
        根据键找出对应的值，若不存在此键则返回空值
        '''
        ArrIndex = self.getIndex(key)
        head = self.Array[ArrIndex]
        # 非空则查找是否存在此键，存在则返回值
        while head != None:
            if head.key == key:
                return head.value
            head = head.nextEle
        # 查找完毕，不存在此键
        return None
    
    def remove(self, key:str):
        '''
        删除key对应的键值对，存在键值对则移除并返回值
        若不存在对应键值对则返回空值
        '''
        # 找到键所对应的键值对
        ArrIndex = self.getIndex(key)
        head = self.Array[ArrIndex]
        prev = None
        while head != None:
            if head.key == key:
                break
            prev = head
            head = head.nextEle
        # 未搜到键值对，返回空值
        if head == None:
            return None
        # 找到键值对，则移除该键值对
        self.size -= 1
        if prev != None:
            # 链表对接，以免断链
            prev.nextEle = head.nextEle
        else:
            # prev为空意味着首位就是目标，下一位移入数组顶替位置即可
            self.Array[ArrIndex] = head.nextEle
        return head.value     
    
    def getSize(self):
        '''
        查看哈希表内元素个数
        '''
        return self.size
    
    def isEmpty(self):
        '''
        检查哈希表是否为空
        '''
        return self.size == 0
