# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:22:41 2020

@author: Administrator
"""

# 链表堆栈，只有一个进出口(存取索引)

class StackNode():
    def __init__(self, value:int, nextVal=None):
        '''
        初始化函数，链表节点，值和指向下一个的指针两个属性
        '''
        self.value = value
        self.nextVal = nextVal

class ListStack():
    def __init__(self, top=None):
        '''
        初始化函数，链表堆栈，单属性top表示待存取的对象
        '''
        self.top = top
    
    def push(self, value:int):
        '''
        装入元素，区分空与非空情况
        '''
        newNode = StackNode(value)
        # 空堆栈直接加入
        if self.top == None:
            self.top = newNode
        # 非空需要进行交换
        else:
            temp = self.top
            self.top = newNode
            newNode.nextVal = temp
    
    def pop(self):
        '''
        从堆栈取出元素作为返回值，若无元素则报错并返回None
        取出的元素将不再存放于堆栈中
        '''
        if self.top == None:
            print("empty")
            return None
        popped = self.top.value
        self.top = self.top.nextVal
        return popped
    
    def peek(self):
        '''
        从堆栈中读取顶部元素，若无元素则报错并返回None
        读取的元素仍在堆栈中
        '''
        if self.top == None:
            print("empty")
            return None
        else:
            return self.top.value
    
    def isEmpty(self):
        '''
        通过检查待存取元素是否空，判断堆栈是否空
        '''
        return self.top == None
    
