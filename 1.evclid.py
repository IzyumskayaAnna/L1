print ("Введите а")
a = int(input())
print ("Введите b")
b = int(input())

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print("Наибольший общий делитель")
print(a + b)
