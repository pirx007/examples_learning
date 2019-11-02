MAX_RANGE = 10
proper_divisors_sum = 0

for number in range(1, MAX_RANGE):
    print("=====================")
    print("For number " + str(number) + ":")
    proper_divisors_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            #print("number=" + str(number))
            print("divisor=" + str(divisor))
            proper_divisors_sum = proper_divisors_sum + divisor
    print("---------------------")
    print("proper_divisors_sum=" + str(proper_divisors_sum))
            