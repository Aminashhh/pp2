def Palindrome(a):
    if a == a[::-1]:
        print('palindrome')
    else:
        print('not palindrome')
Palindrome(input())