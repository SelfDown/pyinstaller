#!/usr/bin/env python
# -*- coding: utf_8 -
def getData(collection):
	print collection

	note = collection['note']

	if not  (note or note['GUID'] or note['COLOR'] or note['FILE_URL'] or note['RESOURCE_ID'] or note['CONTENT']) :
		print "error"
		return {"data":"add failed","success":False}

	if(collection['way']=="sqlite"):
		import uuid
		import sqlite3
		import time
		conn=sqlite3.connect(str(collection['url']))  
		c=conn.cursor()
		sql = "insert into notes(ID,GUID,COLOR,FILE_URL,RESOURCE_ID,CONTENT,CREATE_TIME) values('"+str(uuid.uuid1())+"','"+str(note['GUID'])+"','"+str(note['COLOR'])+"','"+str(note['FILE_URL'])+"','"+str(note['RESOURCE_ID'])+"','"+str(note['CONTENT'])+"','"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"')";
		c.execute(sql)
		conn.commit()
		return {"data":"add success","success":True}

	return {"data":"add failed","success":False}