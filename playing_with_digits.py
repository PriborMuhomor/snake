def dig_pow(n, p):
    n_dubl = n
    list_of_digits = []

    while n_dubl!=0:
        current_length = 10**(len(str(n_dubl))-1)
        list_of_digits.append(n_dubl//current_length)
        n_dubl = n_dubl%current_length

    temp_result = 0

    for index in range(0, len(list_of_digits)):
        temp_result+=list_of_digits[index]**(p+index)

    answer = temp_result//n

    if temp_result%n == 0:
        return answer
    return -1


print(dig_pow(89, 1))

print(dig_pow(695, 2))

print(dig_pow(46288, 51))