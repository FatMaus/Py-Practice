# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:33:24 2020

@author: Administrator
"""

# 链表队列

class QueueNode():
    def __init__(self, value:int, nextVal=None):
        '''
        两个属性，值与下一个的指针
        '''
        self.value = value
        self.nextVal = nextVal
    
class ListQueue():
    def __init__(self, front=None, rear=None):
        '''
        两个属性，队列前端元素、队列后端元素
        '''
        self.front = front
        self.rear = rear
        
    def enqueue(self, value:int):
        '''
        向队列中添加元素
        '''
        newNode = QueueNode(value)
        # 向空队列添加
        if self.rear == None:
            self.rear = newNode
            self.front = self.rear
        # 向非空队列
        else:
            self.rear.nextVal = newNode
            self.rear = newNode
    
    def dequeue(self):
        '''
        提取队列中的元素，空队列直接报错
        非空队列返回提取值，提取后不再存在队列中
        '''
        if self.front == None:
            print("empty")
            return None
        frontNode = self.front
        self.front = self.front.nextVal
        # 提取后变为空队列时，首位等同
        if self.front == None:
            self.rear = None
        return frontNode.value
    