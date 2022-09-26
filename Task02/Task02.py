# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'x = , {x}, y = , {y}, z = , {z} ')
            result = bool(-(x and y and z) == -x or -y or -z)
            print('"¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z" is', result, '\n')


