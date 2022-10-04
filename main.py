"""
print("Hello, World!")
"""
""""
x = 5
y = 30
s = x + y
print(s)
"""
"""
x = "he"
y = "llo"
s = x + y
print(s)
"""
""""
import datetime
print(datetime.date.today())
"""
"""
a = int(input("Число сюююда:"))
b = int(input("Число сюююда:"))
act = input ("Че делаем? Сложим-  + ? Умножим-  * ?:")
if act =="+":
    print(a + b)
elif act =="*":
    print(a * b)
"""
"""
a = int(input("Число сюдаааааааа:"))
res=1
for i in range(1, a + 1):
    res *= i
print("Факториал:", res)
"""

"""
def factorial(x, res = 1):
    for i in range(1, x + 1):
        res *= i
    return(res)
print(factorial(6))
"""
file = open("ygy.txt","w+")
for x in range(1,101):
    if x %3 == 0 and x %5 == 0:
        file.write("Hello World\n")
    elif x %5 == 0:
        file.write("World\n")
    elif x %3 == 0:
        file.write("Hello\n")
    else:
        file.write(str(x)+"\n")
file.close()





