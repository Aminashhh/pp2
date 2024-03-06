def check(tup):
    return all(tup)


tuple1 = (True, True, True)
tuple2 = (True, False, True)

print(check(tuple1))  
print(check(tuple2))