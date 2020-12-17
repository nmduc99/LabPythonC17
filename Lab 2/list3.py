lst = []
n = int(input('so phan tu:' ))
for i in range(n):
	lst.append(int(input()))
for i in range(len(lst)):
	for j in range(i):
		if lst[i] < lst[j]:
			tmp = lst[i]
			lst[i] = lst[j]
			lst[j] = tmp
print(lst)