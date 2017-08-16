#coding:utf-8
import random

def compare_size(x,i):
	if i<x:
		print "你猜错了，你输入的数小了"
		return False
	elif i==x:
		print "你猜对了。"
		return True
	else :
		print "你猜错了，你输入的数大了"
		return False


if __name__=="__main__":
	x = random.randint(0,100);
	print "请输入你猜的数："
	i = int(raw_input())
	while(not compare_size(x,i)):
		print "请输入你猜的数："
		i = int(raw_input())

