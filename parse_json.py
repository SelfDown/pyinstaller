#!/usr/bin/env python
# -*- coding: utf_8 -
def parseJSON(words,iterator):
	names = words.split(",")
	data = [dict(zip(names, d)) for d in iterator]
	return data