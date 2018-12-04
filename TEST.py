#!/usr/bin/env python
# -*- coding: utf_8 -
import pyhdb
import json
import sys
import sqlite3
conn = sqlite3.connect("position.db")
cursor = conn.cursor()
for item in range(50):
	sql ='insert into platform_important_typical_events values("1'+str(item)+'","2'+str(item)+'","3'+str(item)+'","4'+str(item)+'","5'+str(item)+'","6'+str(item)+'","7'+str(item)+'","8'+str(item)+'","9'+str(item)+'","10'+str(item)+'","11'+str(item)+'","12'+str(item)+'","1'+str(item)+'","2'+str(item)+'","3'+str(item)+'","4'+str(item)+'","5'+str(item)+'","6'+str(item)+'","7'+str(item)+'","8'+str(item)+'","9'+str(item)+'","10'+str(item)+'")'
	print sql
	cursor.execute(sql)
conn.commit()