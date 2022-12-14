# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Формула: AB = √(xb - xa)2 + (yb - ya)2
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

print("Введите координаты первой точки: ")
x1 = int(input("x = "))
y1 = int(input("y = "))

print("Введите координаты второй точки: ")
x2 = int(input("x = "))
y2 = int(input("y = "))

ab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f'Расстояние между точками на плоскости = ', ab)
