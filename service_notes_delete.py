#!/usr/bin/env python
# -*- coding: utf_8 -
def getData(collection):
	print collection
	if not collection["ID"] :
		print "error"
		return {"data":"ID is null","success":False}

	if(collection['way']=="sqlite"):
		import uuid
		import sqlite3
		import time
		conn=sqlite3.connect(str(collection['url']))  
		c=conn.cursor()
		sql = "delete from notes where id = '"+collection["ID"]+"'"
		c.execute(sql)
		conn.commit()
		return {"data":"delete success","success":True}

	return {"data":"delete failed","success":False}