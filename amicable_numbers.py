print("test")
MAX_RANGE = 300

for x in range(1, MAX_RANGE):
    print("For number" + str(x))
    for y in range(1, x):
        if x % y == 0:
            print(y)