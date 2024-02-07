def filter_prime(a):
    result = list(filter(lambda x: sum([x%i == 0 for i in range(1,x+1)]) == 2, a))
    print(result)
filter_prime([17,8,9,20,97,12])

