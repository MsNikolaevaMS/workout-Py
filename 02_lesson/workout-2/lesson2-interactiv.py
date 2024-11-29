# получить оценку от пользователя

rate_as_str = input("Оцените работу оператора от 1 до 5:  ")
rate = int(rate_as_str)


# проверить оценку от 1 до 5

if (rate < 1):
    rate = 1


if (rate > 5):
    rate = 5


print(rate)


# в зависимости от оценки предложить обратную связь.

feedback = ''

if rate == 1:
    feedback = input("рааскажите, что вам не понравилось:")
elif rate == 2:
    feedback = input("рааскажите, что вас не устроило:")
elif rate == 3:
    feedback = input("рааскажите, что нам улучшить:")
elif rate == 4:
    feedback = input("рааскажите, что испортило впечатление:")
else:
    feedback = input("рааскажите, за что нам поблагодарить оператора:")


print(feedback)