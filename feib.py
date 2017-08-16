#coding:utf-8


def forb(n):
	if n==1:
		n=1
	if n==2:
		n=1
	if n>1:
		n = forb(n-2) + forb(n-1)
	return n

if __name__=="__main__":
	n = int(raw_input("请输入第n项forb数列："))
	forb = forb(n);
	print("第%d项forb数列的值为%d"%(n,forb))

