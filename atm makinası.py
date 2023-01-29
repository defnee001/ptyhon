print("""
***********************************
atm makinesine hosgeldiniz

islemler;
1. bakiye sorgulama
2. para yatırma
3. para cekme
programdan çıkmak için 'q' ya basın.
************************************

""")
bakiye =1000
while True:
    islem=input("islemi seciniz...")
    if (islem=="q"):
        print("yine bekleriz")
        break
    elif (islem =="1"):
        print("bakiyeniz {} tl dir".format(bakiye))

    elif (islem == "2"):
        miktar=int(input("miktarı giriniz:"))
        bakiye += miktar

    elif (islem == "3"):
        miktar=int(input("miktarı giriniz:")
        if (bakiye - miktar < 0):
            print("böyle bir miktar cekemezsiniz")
            continue
            bakiye -= miktar

    else:
        print("gecersiz islem")




