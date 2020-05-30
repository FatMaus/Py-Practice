# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:21:43 2020

@author: FatMaus
"""

# 优先队列

class Node():
    def __init__(self, value:int, priority:int, nextEle=None):
        '''
        优先队列的节点元素，由值、优先级、下一个节点的指针三个元素组成
        '''
        self.value = value
        self.priority = priority
        self.nextEle = nextEle
        
class PriorityQueue():
    def __init__(self, head=None):
        '''
        优先队列中只需要记住头节点
        '''
        self.head = head
    
    def push(self, value:int, priority:int):
        '''
        插入新元素，逐个比较找到合适的位置
        复杂度O(N)
        '''
        newNode = Node(value, priority)
        # 空队列直接填入头节点
        if self.head == None:
            self.head = newNode
            return
        cur = self.head
        # 优先级最高直接替代头节点
        if self.head.priority < priority:
            newNode.nextEle = self.head
            self.head = newNode
        else:
            # 找到某节点优先级较高但下一个节点优先级较低
            while cur.nextEle != None and cur.nextEle.priority > priority:
                cur = cur.nextEle
            newNode.nextEle = cur.nextEle
            cur.nextEle = newNode
    
    def peek(self):
        '''
        查看优先级最高的节点，直接返回头节点即可
        '''
        return self.head
    
    def pop(self):
        '''
        取出优先级最高的节点，取出后节点不再存在队列中
        '''
        # 空队列返回空值
        if self.head == None:
            return None
        ret = self.head
        self.head = self.head.nextEle
        return ret
    
    def isEmpty(self):
        '''
        判断队列是否为空
        '''
        return self.head == None
    