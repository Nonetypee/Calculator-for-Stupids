##BU DOSYA ÜZERİNDE DEĞİŞİKLİK YAPMANIZ PROGRAMIN ÇALIŞMAMASINA SEBEP OLUR!
##NONETYPE

def equivilent_solver(a,b,c):

    diskarment = b ** 2 - (4 * a * c)

    x1 = (-b + (diskarment ** (1 / 2))) / (2 * a)
    x2 = (-b - (diskarment ** (1 / 2))) / (2 * a)
    return print("""Kökleriniz {} ve {} 'dir""".format(x1, x2))

def circle_area_finder_with_pi3 (r):
    pi = 3
    circle_area = pi * (r ** 2)
    return print("Daire'nin alanı {} metrekare/santimetrekare'dir".format(circle_area))

def circle_area_finder_with_pi314 (r):
    pi = 3.14
    circle_area = pi * (r ** 2)
    return print("Daire'nin alanı {} metrekare/santimetrekare'dir".format(circle_area))

def archlenght_finder_with_pi3 (r,o):
    pi = 3
    archlenght = 2 * pi * r * (o / 360)
    return print("Yay'ın uzunluğu: {}".format(archlenght))

def archlenght_finder_with_pi3 (r,o):
    pi = 3.14
    archlenght = 2 * pi * r * (o / 360)
    return print("Yay'ın uzunluğu: {}".format(archlenght))

def kinetic_energy_formula_finder():
    x = int(input("""Hangi değişkeni bulmak istediğinizi seçiniz;
                    1.V
                    2.M
                    3.EK
                    """))
    if x == 1:
        EK = int(input("EK değerini giriniz:"))
        M = int(input("Kütle değerini giriniz:"))
        answer = (EK * 2 / M) ** (1 / 2)
        return print("Cismin hızı : {}".format(answer))
    elif x == 2:
        EK = int(input("EK değerini giriniz:"))
        V = int(input("Hız değerini giriniz:"))
        answer = (2 * EK) / (V ** 2)
        return print("Cismin kütlesi : {}".format(answer))

    elif x == 3:
        V = int(input("Hız değerini giriniz:"))
        M = int(input("Kütle değerini giriniz:"))
        answer = (1 / 2) * M * (V ** 2)
        return print("EK değeri: {}".format(answer))
    
        
