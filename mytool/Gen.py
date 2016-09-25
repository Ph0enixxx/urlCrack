#list all the short code
#multi thread
#create Random
#so slow..use C instead of Py here
def gen(start='000000',end='zzzzzz'):
	text = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for a in text:
		for b in text:
			for c in text:
				for d in text:
					for e in text:
						for f in text:
							lst = [a,b,c,d,e,f]
							yield "".join(lst)


if __name__ == '__main__':
	x = gen()
	# for i in x:
	# 	pass
	# 	#print(i)
	# print("ok")
	# for i in range(1,1000):
	# 	print(x.__next__())
	print(next(x))
	print(next(x))
	print(next(x))
	print(next(x))