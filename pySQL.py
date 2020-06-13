# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:50:31 2020

@author: FatMaus
"""

import pymysql

class SQLOperation():
    def __init__(self, host:str, username:str, password:str, database:str):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
    
    def createTable(self, sqlStr):
        '''
        执行创建表操作
        '''
        db = pymysql.connect(self.host, self.username, self.password, self.database)
        cursor = db.cursor()
        cursor.execute(sqlStr)
        db.close()
    
    def query(self, sqlStr):
        '''
        查询操作，返回的是元素为列表的列表
        '''
        db = pymysql.connect(self.host, self.username, self.password, self.database)
        cursor = db.cursor()
        try:
            cursor.execute(sqlStr)
            result = cursor.fetchall()
            return result
        except:
            db.rollback()
        db.close()
         
    def insertAndUpdate(self, sqlStr):
        '''
        插入、更新和删除都可以通过此方法完成
        '''
        db = pymysql.connect(self.host, self.username, self.password, self.database)
        cursor = db.cursor()
        try:
            cursor.execute(sqlStr)
            db.commit()
        except:
            db.rollback()
        db.close()
 
# 简易测试
SQLObj = SQLOperation("localhost", "username", "password", "pytest")
SQLObj.createTable("CREATE TABLE sorceries(\
                   id BIGINT NOT NULL PRIMARY KEY,\
                   name VARCHAR(255),\
                       memoryCell INT,\
                           useTime INT);")
SQLObj.insertAndUpdate('INSERT INTO sorceries(id,name,memoryCell,useTime)\
                       VALUES(1,"Soul Arrow",1,30);')
# ...
ret = SQLObj.query("SELECT name,useTime FROM sorceries WHERE id>0;")
for row in ret:
    print(row)
SQLObj.insertAndUpdate("DELETE FROM sorceries WHERE id=1")