# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:07:39 2020

@author: Administrator
"""

# 链表节点，存储元素本身和下一个元素的信息(指针)

class Node():
    # 值与下一个的地址，两个属性(单链表)
    def __init__(self, elem, nextEle=None):
        self.elem = elem
        self.nextEle = nextEle

# 链表

class LinkListNode():
    # 首位头元素、末位尾元素，长度三个属性
    def __init__(self, head=None, tail=None, size=0):
        self.head = head
        self.tail = tail
        self.size = size
    
    # 增加元素(末位增加)
    def append(self, number:int):
        newNode = Node(number)
        # 没有元素的时候直接添加到头，且头尾相同
        if self.size == 0:
            self.head = newNode
            self.tail = self.head
            self.size += 1
            return
        # 有头无尾，变成尾
        elif self.tail == None:
            self.tail = newNode
        # 有头有尾，直接变成尾
        else:
            self.tail.nextEle = newNode
            self.tail = newNode
        self.size += 1
        
    # 按位置索引插入元素
    def insert(self, position:int, number:int):
        # 防止索引超出报错
        if position > self.size:
            return
        newNode = Node(number)
        # 首位添加
        if position == 0:
            newNode.nextEle = self.head
            self.head = newNode
            if self.tail == None:
                self.tail = newNode
            self.size += 1
        # 末位添加直接调用append方法
        elif position == self.size:
            self.append(number)
        # 其他位置添加
        else:
            prev = self.head
            for i in range(position):
                prev = prev.nextEle
            newNode.nextEle = prev.nextEle
            prev.nextEle = newNode
            self.size += 1
            
    # 按值查找索引(不存在则返回-1)
    def getIndex(self, number:int):
        cur = self.head
        for i in range(self.size):
            if cur.elem == number:
                return i
            else:
                cur = cur.nextEle
        return -1
        
    # 按值删除元素
    def delete(self, number:int):
        # 删除的是头元素时
        if self.head.elem == number:
           self.head = self.head.nextEle
           self.size -= 1
           # 删光时保证头尾相同
           if self.size == 0:
               self.tail = self.head
        # 删除非头元素
        else:
            prev = self.head
            cur = self.head
            # 一位一位向后查找
            while prev != None and cur != None:
                if cur.elem == number:
                    # 若是尾元素直接去尾
                    if cur == self.tail:
                        self.tail = prev
                    # 非尾元素要进行指针交接，以免断点
                    prev.nextEle = cur.nextEle
                    self.size -= 1
                    return
                # 继续向后匹配
                prev = cur
                cur = cur.nextEle
                
    # 按新旧值更新元素(更改)
    def update(self, old:int, new:int=old:int):
        # 从头开始匹配
        cur = self.head
        for i in range(self.size):
            # 匹配到直接更新值，然后返回索引
            if cur.elem == old:
                cur.elem = new
                return i
            # 不匹配继续推进匹配
            else:
                cur = cur.nextEle
        # 遍历完仍未匹配到则返回-1
        return -1
    
    # 遍历元素，并装入数组打印
    def display(self):
        cur = self.head
        printList = []
        for i in range(self.size):
            printList.append(cur.elem)
            cur = cur.nextEle
        print(printList)

# 简易测试
al = LinkListNode()
for i in range(10):
    al.append(i)

al.display()
