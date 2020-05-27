# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:02:47 2020

@author: Administrator
"""

# 数组堆栈，只有一个进出口(存取索引)，先进后出后进先出

class ArrStack():
    def __init__(self, top:int=-1, CAP:int=10, stack:list=[]):
        '''
        初始化函数，对象有三个属性
        顶部元素位置(存取索引)top，容量CAP，数组stack
        '''
        self.top = top
        self.CAP = CAP
        self.stack = stack
        
    def push(self, value:int):
        '''
        向堆栈添加元素，若满溢则报错
        '''
        if self.top >= self.CAP - 1:
            print("overflow")
            return False
        self.top += 1
        self.stack[self.top] = value
        return True
    
    def pop(self):
        '''
        从堆栈取出元素作为返回值，若无元素则报错并返回0
        取出的元素将不再存放于堆栈中
        '''
        if self.top < 0:
            print("empty")
            return 0
        elem = self.stack[self.top]
        self.top -= 1
        return elem
    
    def peek(self):
        '''
        从堆栈中读取顶部元素，若无元素则报错并返回0
        读取的元素仍在堆栈中
        '''
        if self.top < 0:
            print("empty")
            return 0
        elem = self.stack[self.top]
        return elem
    
    def isEmpty(self):
        '''
        检查堆栈是否为空
        '''
        return self.top < 0
    
