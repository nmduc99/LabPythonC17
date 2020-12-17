import math
from  math import  sqrt
# câu 1
arr=[]
for i in range(10,201):
	if(i % 7 == 0) and (i % 5 !=0):
		arr.append (str(i))
print(',' .join(arr))

# cau 2
n = int(input(('nhap so : ')))
def giaithua(n):
	
	if n ==0:
		return 1
	return n * giaithua(n-1)
print (giaithua(n))

# cau 3

x = int(input(('nhap so : ')))
d = dict()
for  i in range(1,n + 1):
	d[i] = i*i
print(d)

# cau 4
def convert_number(n,b):
	if(n < 0 or b< 2  or b>16):
		return ""
	sb = ""
	m = 0
	remainde = n
	while (remainde >0):
		if( b > 10):
			m = remainde %b 
			if ( m >=10):
				sb = sb +str(chr(55 +m))
			else:
				sb =sb + str(m)
		else:
			sb = sb + str(remainde % b )
		remainde = int(remainde / b)
	return "".join(reversed(sb))
n = int (input("nhap so nguyen duong n = "))
print("he co so so 2 ",n ," la" ,convert_number(n,2))
print("he co so so 16 ",n ," la" ,convert_number(n,16))
# cau 5
def fibnacci(n):
	f0 = 0
	f1 =1 
	fn = 1
	if(n<-0):
		return -1
	elif (n ==0 or n ==1):
		return n
	else:
		for  i in range (2,n):
			f0 = f1
			f1 = fn 
			fn = f0 +f1
		return fn
print("10 so dau cua finacci")
sb = ""
for  i in range (2,10):
	sb = sb + str(fibnacci(i))+','
print(sb)
# cau 6

def lietke(n):
	# so nguyen n<2 khong phai la so nguyen to
	if(n<2):
		return False;
	# check so nguyen to khi n>= 2
	squareRoot= int(math.sqrt(n));
	for i in range(2,squareRoot +1):
		if (n%i==0):
			return False;
	return True;
n= int(input("Nhập số nguyên dương n = "));
print("Tất cả các số nguyên tố nhỏ hơn", n, "là:");
sb ="";
if (n>=2):
	sb=sb+"2"+" ";
for i in range (3, n+1):
	if (lietke(i)):
		sb= sb+str(i) +" ";
	i= i +2
print (sb);
# cau 7
def demsonuyento(n):
	# so nguyen n < 2 khong phai la so nguyen to
	if (n < 2):
		return False;
 
	# check so nguyen to khi n >= 2
	squareRoot = int(math.sqrt(n));
	for i in range(2, squareRoot + 1):
		if (n % i == 0):
			return False;
	return True;
 
n = int(input("Nhập số nguyên dương n = "));
print (n, "Số nguyên tố đầu tiên là:");
dem = 0; # đếm số số nguyên tố
i = 2;   # tìm số nguyên tố bắt dầu từ số 2
sb = "";
while (dem < n):
	if (demsonuyento(i)):
		sb = sb + str(i) + " ";
		dem = dem + 1;
	i = i + 1;
print(sb);

# cau 8

def demsont(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
 
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;
 
print ("Liệt kê tất cả số nguyên tố có 5 chữ số:");
dem = 0;
for i in range(10001, 99999):
    if (demsont(i)):
        print(i);
        dem = dem + 1;
print("Tổng các số nguyên tố có 5 chữ số là:", dem);


# cau 9
def tinhtongchucai(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
 
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", tinhtongchucai(n));

# cau 10
values= input ("Nhập vào các giá trị:")
l= values.split(",")
t=tuple(l)
print(l)
print(t)



