import random
n = int(input("กรอกตัวเลข: "))
x = random.randint(1,100)

while True:
    

    if n > x:
        print("มากไป")
        n = int(input("กรอกตัวเลข: "))
    elif n < x:
        print("น้อยไป")
        n = int(input("กรอกตัวเลข: "))
    else:
        print("ถูกต้องนะคร้าบ")
        break
    







