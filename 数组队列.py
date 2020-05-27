# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:33:12 2020

@author: Administrator
"""

# 数组队列，先存先取

class ArrQueue():
    def __init__(self, CAP=10, front=0, rear=0, size=0, Array=[]):
        '''
        初始化函数，五个属性，主要指定容量
        队列容量CAP、队列前端索引front、队列末端索引rear、队列长度size、容器Array
        '''
        self.CAP = CAP
        self.front = front
        self.rear = rear
        self.size = size
        self.Array = Array
    
    def isFull(self):
        '''
        方法，检查是否装满
        '''
        return self.size == self.CAP
    
    def isEmpty(self):
        '''
        方法，检查队列是否为空
        '''
        return self.size == 0
    
    def enqueue(self, item:int):
        '''
        入队函数，给队列末位增加元素，若队列已满则不操作
        通过求余操作实现循环队列
        '''
        if self.isFull():
            print("queue is full")
            return
        self.Array[self.rear] = item
        self.rear = (self.rear + 1) % self.CAP
        self.size += 1
        print("enqueue successed")
    
    def dequeue(self):
        '''
        从队列头部提取元素，被取出的元素不再存放于队列
        通过求余操作实现循环队列
        '''
        if self.isEmpty():
            print("queue is empty")
            return
        ret = self.Array[self.front]
        self.front = (self.front + 1) % self.CAP
        self.size -= 1
        return ret
    
    def peek(self):
        '''
        查看队列头部元素，查看后元素仍存于队列
        '''
        if self.isEmpty():
            print("queue is empty")
            return
        return self.Array[self.front]
        
