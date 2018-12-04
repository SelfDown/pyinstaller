#!/usr/bin/env python
# -*- coding: utf_8 -
def getPosition(data,SERVICE_NAME,ID):
	import sqlite3
	conn = sqlite3.connect('position.db')
	c = conn.cursor()	
	for item in data:
		sql= "SELECT x,y,z FROM POSITIONS WHERE SERVICE_NAME = '"+str(SERVICE_NAME)+"' and table_or_view_id = '"+str(item[ID])+"' order by create_time desc"
		#print sql
		c.execute(sql)
		posi = c.fetchone()
		if posi:
			posi = list(posi)
			item['X'] = posi[0]
			item['Y'] = posi[1]
			item['Z'] = posi[2]
	return data
def addPosition(SERVICE_NAME,ID,X,Y,Z):
	import sqlite3
	import time
	conn = sqlite3.connect('position.db')
	c = conn.cursor()
	sql = "SELECT ID FROM POSITIONS WHERE SERVICE_NAME = '"+str(SERVICE_NAME)+"' and table_or_view_id = '"+str(ID)+"' order by create_time desc"
	print sql
	c.execute(sql);
	data = c.fetchone()
	# 数据存在就更新
	if data:
		updateSql = " update POSITIONS\n"\
					+"set x="+str(X)+",y="+str(Y)+",z="+str(Z)+",create_time="+str(time.time())+"\n"\
					+"where SERVICE_NAME = '"+SERVICE_NAME+"' and table_or_view_id = '"+ID+"'"
		c.execute(updateSql)
		conn.commit()
		c.close()
	else:
		insertSql = "insert into POSITIONS(ID,SERVICE_NAME,TABLE_OR_VIEW_ID,X,Y,Z,CREATE_TIME) values('"+str(time.time())+"','"+SERVICE_NAME+"','"+ID+"','"+str(X)+"','"+str(Y)+"','"+str(Z)+"','"+str(time.time())+"')"
		c.execute(insertSql)
		conn.commit()
		c.close()
	return True