"""birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10

    return onlar[ikinci] + " " + birler[birinci]


sayı = int(input("Sayı:"))

print(okunus(sayı))"""


def pisagor_bulma():
    pisagor_listesi = list()
    for i in range(1, 101):
        for j in range(1, 101):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)):
                pisagor_listesi.append((i, j, int(c)))

    return pisagor_listesi


for i in pisagor_bulma():
    print(i)






