def square(side):
    area = side * side
    return round(area)


side_str = input("Введите длину стороны квадрата: ")


try:
    side = float(side_str)
except ValueError:
    print("Ошибка: Пожалуйста, введите числовое значение для стороны.")
    exit()


area = square(side)
print("Площадь квадрата:", area)
