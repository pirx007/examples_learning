MAX_RANGE = 300
proper_divisors_sum = 0
amicable_numbers_candidates = []

for number in range(1, MAX_RANGE):
    print("=====================")
    print("For number " + str(number) + ":")
    proper_divisors_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            # print("number=" + str(number))
            # print("divisor=" + str(divisor))
            proper_divisors_sum = proper_divisors_sum + divisor
    print("---------------------")
    print("proper_divisors_sum=" + str(proper_divisors_sum))
    amicable_numbers_candidates.append(proper_divisors_sum)

print(amicable_numbers_candidates)
for index, value in enumerate(amicable_numbers_candidates):
    if value in index:
        print("index = " + str(index))
        # print("value = " + str(value))
        # if amicable_numbers_candidates[value] == 
            