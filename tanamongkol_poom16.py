
n1 = int(input("กรอกแม่สูตรคูณเริ่มต้น (n1): "))
n2 = int(input("กรอกแม่สูตรคูณสุดท้าย (n2): "))

print("\n--- เริ่มแสดงแม่สูตรคูณ ---")


for i in range(n1, n2 + 1):
    print(f"\n--- แม่  ---")

    for j in range(1, 13):
        result = i * j
        print(f"{i} x {j} = {result}")



































