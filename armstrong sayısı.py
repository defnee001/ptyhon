a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))

i= 1000*a+100*b+10*c+d
print("sayi:",i)
if (a**4+b**4+c**4+d**4==i):
    print("armstrong.")
else:
    print("armstrong degil")
