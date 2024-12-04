# Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
# Функция должна печатать числа от 1 до n. При этом: если число делится на 3, печатать fizz;
# если число делится на 5, печатать Buzz;
# если число делится на 3 и на 5, печатать FizzBuzz.


def fizz_buzz(number):
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


number = int(input("Введите число n: "))
fizz_buzz(number)
