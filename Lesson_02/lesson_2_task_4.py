def fizz_buzz(n):
    k = 1
    while k <= n:
        if k % 3 == 0 and k % 5 == 0:
            print("FizzBuzz")
        elif k % 5 == 0:
            print("Buzz")
        elif k % 3 == 0:
            print("Fizz")
        else:
            print(k)
        k += 1


X = int(input("Введите число: "))
fizz_buzz(X)
