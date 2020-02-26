num = input().split()

l = []
rst1 = []
rst2 = []
rst3 = []
rst4 = []
for i in range(int(num[0])):
    stu = input().split()
    l.append(stu)

l.sort(key=lambda student: student[0], reverse=False)
l.sort(key=lambda student: (int(student[1]) + int(student[2]), student[1]), reverse=True)

for k in l:
    if int(k[1]) >= int(num[2]) and int(k[2]) >= int(num[2]):
        rst1.append(k)
    elif int(k[1]) >= int(num[2]) and int(k[2]) >= int(num[1]):
        rst2.append(k)
    elif int(k[1]) >= int(num[1]) and int(k[2]) >= int(num[1]) and int(k[1]) > int(k[2]):
        rst3.append(k)
    elif int(k[1]) >= int(num[1]) and int(k[2]) >= int(num[1]):
        rst4.append(k)
print(len(rst1) + len(rst2) + len(rst3) + len(rst4))
for r1 in rst1:
    print(" ".join(r1))
for r2 in rst2:
    print(" ".join(r2))
for r3 in rst3:
    print(" ".join(r3))
for r4 in rst4:
    print(" ".join(r4))