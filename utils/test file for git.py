a = 2
b = 3
c = 4

d = min(a,b,c)
s_square = float(d**2)
p = (a + b + c) /2
s_triangle = float((p*(p-a)*(p-b)*(p-c))**0.5)

if s_square > s_triangle:
    print("Площадь квадрата больше площади треугольника.")
elif s_square < s_triangle:
    print("Площадь треугольника больше площади квадрата.")
else:
    print("Фигуры равны по площади")