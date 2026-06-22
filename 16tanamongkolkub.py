print("โปรเเกรมคำนวณคะเเนน\n")
point_math=int(input("คะเเนนวิชาคณิตศาสตร์: "))
point_science=int(input("คะเเนนวิชาวิทยาศาสตร์: "))
point_physical=int(input("คะเเนนวิชาดนตรี: "))
totalpoint=(point_math+point_science+point_physical)
print("\nคะเเนนรวมทั้ง3วิชา:  ", totalpoint)
if totalpoint >=80: 
    print("ดีเยี่ยม")

elif totalpoint >=60: 
    print("ผ่าน")
    
else: 
    print("ควรปรับปรุง")

Average=(totalpoint/3)
print("\nคะเเนนเฉลี่ยทั้ง3วิชา:  ", Average )
  
print("นาย ธนมงคล ภูด่านงัว ม.4/4 เลขที่16")