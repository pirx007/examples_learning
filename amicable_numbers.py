MAX_RANGE = 10
right_divisor = 0
sum_of_y = 0

for x in range(1, MAX_RANGE):
    print("===================")
    print("For number " + str(x))
    sum_of_y = 0
    for y in range(1, x):
        if x % y == 0:
            print("x=" + str(x))
            print("y=" + str(y))
            right_divisor = y
            sum_of_y = sum_of_y + y
    print(sum_of_y)
            