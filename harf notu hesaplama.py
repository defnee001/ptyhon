vize1=int(input("vize1:"))
vize2=int(input("vize2:"))
final1=int(input("final1:"))

hesap=(30*vize1/100)+(30*vize2/100)+(40*final1/100)
x1=(hesap)

print("hesapla{}|\n".format(x1))

if(x1>=90):
    print("AA")

elif(x1>=85):
    print("BA")

elif (x1 >= 80):
    print("BB")

elif (x1 >= 75):
    print("CB")

elif (x1 >= 70):
    print("CC")

elif (x1 >= 65):
    print("DC")

elif (x1 >= 60):
    print("DD")

elif (x1 >= 55):
    print("FD")

elif (x1 < 55):
    print("FF")
else:
    print("hesaplanamadı...")
