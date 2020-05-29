# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:25:06 2020

@author: FatMaus
"""

# 排序二叉树，又称二分查找树

class TreeNode():
    def __init__(self, value:int, left=None, right=None):
        '''
        排序二叉树的节点，拥有三个属性
        指向左右子树的指针，自身的值
        '''
        self.value = value
        self.left = left
        self.right = right
        
class BST():
    def __init__(self, root=None):
        '''
        排序二叉树只需要记录根节点root
        其余节点依序查找
        '''
        self.root = root
        
    def get(self, key:int):
        '''
        找到与key相同的节点node
        没有相同节点则返回空值
        '''
        cur = self.root
        while cur != None:
            if key < cur.value:
                cur = cur.left
            elif key > cur.value:
                cur = cur.right
            elif cur.value == key:
                return cur
            else:
                print("something wrong")
                break
        return None
    
    def insert(self, key:int):
        '''
        将添加的新元素插入到合适的位置
        '''
        # 空树直接成为根节点
        if self.root == None:
            self.root = TreeNode(key)
            return
        cur = self.root
        parent = None
        # 不断迭代查找，插入符合条件的位置
        while True:
            parent = cur
            if key < parent.value:
                cur = parent.left
                if cur == None:
                    parent.left = TreeNode(key)
                    return
            elif key > parent.value:
                cur = parent.right
                if cur == None:
                    parent.right = TreeNode(key)
                    return
            else:
                # BST不允许两个数值相同的节点存在，连同其他情况，直接报错
                print("something wrong")
                return
            
    def remove(self, key):
        '''
        移除指定的节点
        寻找到节点，若不存在该节点返回False
        找到节点后判断子节点/子树数量，按情况更改树结构
        '''
        # 从根节点开始找，设一个辅助变量存储父节点
        cur = self.root
        parent = cur
        # 辅助boolean以判断目标节点状况
        isLeftChild = False
        while cur != None and cur.value != key:
            parent = cur
            if cur.value > key:
                isLeftChild = True
                cur = cur.left
            else:
                isLeftChild = False
                cur = cur.right
        # 遍历后可能找到节点，也可能未找到，未找到返回False
        if cur == None:
            return False
        # 若该节点是leaf
        if cur.left == None and cur.right == None:
            if cur == self.root:
                self.root = None
            elif isLeftChild:
                parent.left = None
            else:
                parent.right = None
        # 若该节点仅有一个子节点，移除节点后子节点顶上
        # 只有左子节点
        elif cur.right == None:
            if cur == self.root:
                self.root = cur.left
            elif isLeftChild:
                parent.left = cur.left
            else:
                parent.right = cur.left
        # 只有右节点
        elif cur.left == None:
            if cur == self.root:
                self.root = cur.right
            elif isLeftChild:
                parent.left = cur.right
            else:
                parent.right = cur.right
        # 该节点拥有完整(左右)子节点
        else:
            replaceNode = self.getReplace(cur)
            if cur == self.root:
                self.root = replaceNode
            elif isLeftChild:
                parent.left = replaceNode
            else:
                parent.right = replaceNode
            replaceNode.left = cur.left
            replaceNode.right = cur.right
        return True
            
            
    def getReplace(self, node):
        '''
        在左右子树中，找出满足要求的替代节点
        左子树的最大(右)值和右子树的最小(左)值比较，较大者为替代节点
        '''
        leftNode = node.left
        leftParent = node
        rightNode = node.right
        rightParent = node
        while leftNode.right != None:
            leftParent = leftNode
            leftNode = leftNode.right
        while rightNode.left != None:
            rightParent = rightNode
            rightNode = rightNode.left
        if leftNode > rightNode:
            leftParent.right = None
            return leftNode
        else:
            rightParent.left = None
            return rightNode
        
