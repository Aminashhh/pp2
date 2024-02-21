num = int(input("Enter a number: "))

def print_even_numbers(num):
    i=0
    while i!=num:
        if i % 2 == 0:
            print(i, end=", ")
        i+=1

print_even_numbers(num)