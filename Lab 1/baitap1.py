
def mainbt1():
	print("chọn câu : ")
	print("câu 1  ")
	print("câu 2  ")
	print("câu 3  ")
	print("câu 4  ")
	print("câu 5  ")
	print("câu 6  ")
	print("câu 7  ")
	print("câu 8  ")
	print("chọn 0 để kết thúc ")
	n1 = int(input("nhập câu muốn chọn : "))

	if n1 ==1:
		cau1()
		mainbt1()
	elif n1==2:
		cau2()
		mainbt1()
	elif n1==3:
		cau3()
		mainbt1()
	elif n1==4:
		cau4()
		mainbt1()
	elif  n1 ==5:
		cau5()
		mainbt1()
	elif n1==6:
		cau6()
		mainbt1()
	elif n1==7:
		cau7()
		mainbt1()
	elif n1==8:
		cau8()
		mainbt1()
	elif n1==0:
		print("tạm biệt")
	
	else:
		print("chọn không hợp lệ mời bạn chọn lại")
		mainbt1()

def is_abundant(n):

	sum = 0
	for i in range(1, n//2 +1):
		if n % i == 0:
			sum+= i
	if sum > n: 
		return True
	else:
		return False

def evenNum(res):
	s=[]
	for i in res:
		if i % 2 ==0:
			s.append(i)
	print(s)

def power(a, b):
	if b == 0 :
		return 1
	elif b ==1 :
		return a
	else:
		c=a*power(a, b-1) 
		return c
def sumOfAll(n):
	s = 0
	for i in range(1, n//2+1):
		if n % i == 0:
			s += i
	return s 
def Convert(res):
	s=[]
	for i in res:
		s.append(str(i))
	j="".join(s)
	print(j)

def TuMax(str):
	c=[]
	for i in str.split(" "):
		if len(i) >3:
			c.append(i)
	return c

def format(s):
	if len(s)>3:
		if s.endswith("ing")==True:

			s = s+'ly'
			return s
		else:
			s = s+'ing'
			return s
	else:
		return s

def cau1():
	chuoi = str(input("Nhập chuối: "))
	print(TuMax(chuoi))


def cau2():
	res = []
	lengths = int(input("nhập đồ dài của mảng : "))
	for i in range(lengths):
		n = int(input("nhập phần tử của mảng : "))
		res.append(n)

	Convert(res)

def cau3():
	s = str(input("nhập chuối : "))
	c = s[-3:]
	print(format(s))

def cau4():
	n = int(input("nhập n số nguyên dương : "))
	print(sumOfAll(n))

def cau5():
	n = int(input("nhập n : "))
	print(is_abundant(n))


def cau6():
	res = []
	lengths = int(input("nhập đồ dài của mảng : "))
	for i in range(lengths):
		n = int(input("nhập phần tử của mảng : " ))
		res.append(n)
	evenNum(res)



def cau7():
	a = int(input("nhập a : "))
	b = int(input("nhập mũ : "))
	print(power(a, b))

def cau8():
	a = int(input("nhập cạnh a : "))
	b = int(input("nhập cạnh b : "))
	c = int(input("nhập cạnh c : "))

	if a == b and b == c:
		print("Equilateral triangle")
	elif a == b or b == c or c == a and (a + b) > c and (a + c) > b and (b + c) > a:
		print("Isosceles triangle")
	elif (a + b) > c and (a + c) > b and (b + c) > a:
		print("Scalene triangle")


