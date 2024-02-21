num = int(input("Enter a number: "))
def func(num):
    for i in range(num+1):
        if i%3==0 or i%4==0:
            print(i,end=",")

func(num)