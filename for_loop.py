a=[1,2,3,4,5,6, "kapil", "harry"]
for i in range(len(a)):
    print(a[i])

for i in range(0,7,2):
    print(i)
    if(i==3):
        break

for i in range(0,7,2):
    if(i==3):
        continue
    print(i)
    