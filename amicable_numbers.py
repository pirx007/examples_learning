MAX_RANGE = 10
right_divisor = 0
sum_of_y = 0

for x in range(1, MAX_RANGE):
    print("===================")
    print("For number " + str(x))
    for y in range(1, x):
        if x % y == 0:
            print("x=" + str(x))
            print("y=" + str(y))
            right_divisor = y
    sum_of_y =+ right_divisor
            #ok_y = ok_y + y
            #print("ok_y=" + str(ok_y))
print("sum_of_y=" + str(sum_of_y))
 #print("div sum=" + str(ok_y))
            