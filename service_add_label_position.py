#!/usr/bin/env python
# -*- coding: utf_8 -
from position import addPosition
def getData(collection):
	print collection
	st = addPosition(collection['target_service_name'],collection['ID'],collection['X'],collection['Y'],collection['Z'])
	if st:
		return {"data":"add success","success":True}	
	else:
		return {"data":"add failed","success":False}