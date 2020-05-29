# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:37:58 2020

@author: FatMaus
"""

# 二叉树的遍历，运用递归

def preOrderTraversal(root):
    '''
    前序遍历，先访问自身，再访问左子树，最后访问右子树
    '''
    if root == None:
        return
    print(root.value, end = ", ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
    
def postOrderTraversal(root):
    '''
    后序遍历，先访问左子树，再访问右子树，最后访问节点自身
    '''
    if root == None:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.value, end = ", ")

def inOrderTraversal(root):
    '''
    中序遍历，先访问左子树，再访问节点自身，最后访问右子树
    此方法遍历排序二叉树可以获得有小到大的有序结果
    '''
    if root == None:
        return
    inOrderTraversal(root.left)
    print(root.value, end = ", ")
    inOrderTraversal(root.right)