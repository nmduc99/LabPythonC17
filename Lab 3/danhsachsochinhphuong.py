def isSquareNumber(num):
    if number <= 0:
        return False
    else:
        isSquareNum = False
        for i in range(1, number + 1):
            if i * i == number:
                isSquareNum = True
                break
        
        if isSquareNum == True:
            return True
        else:
            return False
import timeit
list_number = [1, 3, 4, 8, 11, 25, 39, 40, 49, 50, 66, 77, 88, 91, 100]
total_time = 0
for number in list_number:
    start = timeit.default_timer()
    result = isSquareNumber(number)
    stop = timeit.default_timer()
    result = isSquareNumber(number)
    print("{} is a square number: {}.".format(number, result))
    total_time += stop - start

print("Elapsed time: {}(second)".format(total_time))
