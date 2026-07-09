print("x", end="\t")
for col in range(1, 13):
    print(col, end="\t")
print()  # ขึ้นบรรทัดใหม่เพื่อเริ่มตัวตาราง

# วนลูปสร้างแถวและคำนวณผลคูณ
for row in range(1, 13):
    print(row, end="\t")  # พิมพ์เลขหัวแถวด้านซ้ายสุด
    
    for col in range(1, 13):
        result = row * col
        print(result, end="\t")  # พิมพ์ผลคูณในแถวนั้นๆ
        
    print()  # << เพิ่มตรงนี้! เพื่อให้ขึ้นบรรทัดใหม่เมื่อจบแต่ละแถว