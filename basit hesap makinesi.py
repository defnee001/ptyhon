print("""********************
Hesap makinesi programı

islemler;

1. toplama islemi

2. cikarma islemi

3. carpma islemi

4. bolme islemi
*************************
""")


a= int(input("birinci sayi:"))
b=int(input("ikinci sayi:"))

islem = input("islemi giriniz:")

if islem =="1":
    hesap1=a+b
    print ("islem{}\n".format(hesap1))

elif islem =="2":
    hesap2=a-b
    print ("islem{}\n".format(hesap2))

elif islem =="3":
    hesap3=a*b
    print ("islem{}\n".format(hesap3))

elif islem =="4":
    hesap4=a/b
    print ("islem{}\n".format(hesap4))

else :
    print("gecersiz islem...:")





