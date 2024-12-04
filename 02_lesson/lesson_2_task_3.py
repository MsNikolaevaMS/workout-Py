def square(side):
    # Вычисляем площадь квадрата
    Square_area = side ** 2
    # Возвращаем округленное вверх значение площади
    return int(Square_area + (1 if Square_area % 1 > 0 else 0))

# Ввод стороны квадрата
side_input = input("Введите сторону квадрата: ")
# Преобразуем введенное значение в float
side = float(side_input)

# Вычисляем площадь и выводим результат
result = square(side)
print(result)