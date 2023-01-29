print("""
***************
boy kilo endeksi hesaplama
***************
""")

boy=float(input("boy:"))
kutle=int(input("kutle:"))

c=((kutle/boy )*boy)
if (c<18.5):
    print("zayıf...")
elif (c>=18.5 and c<25):
    print("normal...")
elif (c>=25 and c<30):
    print("fazla kilolu...")
elif (c>=30):
    print("obez...")
else:
    print("sonuc bulunamadı...")