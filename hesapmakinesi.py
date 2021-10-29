## OKUL DERSLERİ İÇİN KULLANIMI KOLAY BASİT HESAPLAMA MAKİNESİ
## NONETYPE
import maths

print('Hoşgeldiniz, Lütfen yapacağınız işlemi ardından değerlerinizi giriniz.')
print("DESIGNED BY NONETYPE")

print("""
ISLEMLER 
1.DENKLEM KÖKLERİ HESAPLAMA
2.DAİRE ALANI HESAPLAMA (Pi = 3)
3.DAİRE ALANI HESAPLAMA (Pi = 3.14)
4.DAİRE YAYI UZUNLUĞU HESAPLAMA (Pi = 3)
5.DAİRE YAYI UZUNLUĞU HESAPLAMA (Pi = 3.14)
6.KİNETİK ENERJİ HESAPLAMA
""")

while True:
    try:
        while True:
            islem = int(input('Yapacağınız işlemi seçiniz (1,2,3,4,5,6):'))
            if islem == 1:
                a = int(input("Lütfen A'nın katsayısını giriniz:"))
                b = int(input("Lütfen B'nin katsayısını giriniz:"))
                c = int(input("Lütfen C'nin katsayısını giriniz:"))

            elif islem == 2 and 3:
                r = int(input("Daire'nin yarıçapını giriniz:"))

            elif islem == 4:
                r = int(input("Lütfen Daire'nin yarıçapını giriniz."))
                o = int(input("Lütfen Daire Yayını gören Açıyı giriniz."))

            elif islem == 5:
                r = int(input("Lütfen Daire'nin yarıçapını giriniz."))
                o = int(input("Lütfen Daire Yayını gören Açıyı giriniz."))


            elif islem == 6:
                pass



            else:
                ('Hatalı giriş yaptınız.')
                break

            while True:

                if islem == 1:
                    maths.equivilent_solver(a,b,c)
                    break
                    

                elif islem == 2:
                    maths.circle_area_finder_with_pi3(r)
                    break
                elif islem == 3:
                    maths.circle_area_finder_with_pi314(r)
                    break
                elif islem == 4:
                    maths.archlenght_finder_with_pi3(r,o)
                    break
                elif islem == 5:
                    maths.archlenght_finder_with_pi314(r,o)
                    break
                elif islem == 6:
                    maths.kinetic_energy_formula_finder()
                    break
                    





                else:
                    print("Hatalı giriş yaptınız.")
    except:
        print("Hatalı bilgi girdiniz.")
