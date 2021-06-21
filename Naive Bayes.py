from fractions import Fraction
"""
# videodaki soru:
veri = [["kırmızı","spor","yerli","evet"],
        ["kırmızı","spor","yerli","hayır"],
        ["kırmızı","spor","yerli","evet"],
        ["sarı","spor","yerli","hayır"],
        ["sarı","spor","ithal","evet"],
        ["sarı", "SUV","ithal","hayır"],
        ["sarı", "SUV","ithal","evet"],
        ["sarı","SUV","yerli","hayır"],
        ["kırmızı","SUV","ithal","hayır"],
        ["kırmızı","spor","ithal","evet"]]

sinifAdlari = ["Renk","Tip","Üretim","Çalıntı Olması"]
siniflandirilacakOrnek = ["kırmızı","SUV","yerli"]

kararDegeri1 = "evet"
kararDegeri2 = "hayır"

"""
# pdf deki örnek soru:
veri = [["güneşli","sıcak","yüksek","zayıf","hayır"],
        ["güneşli","sıcak","yüksek","şiddetli","hayır"],
        ["bulutlu","sıcak","yüksek","zayıf","evet"],
        ["yağmurlu","ılık","yüksek","zayıf","evet"],
        ["yağmurlu","serin","normal","zayıf","evet"],
        ["yağmurlu","serin","normal","şiddetli","hayır"],
        ["bulutlu","serin","normal","şiddetli","evet"],
        ["güneşli","ılık","yüksek","zayıf","hayır"],
        ["güneşli","serin","normal","zayıf","evet"],
        ["yağmurlu","ılık","normal","zayıf","evet"],
        ["güneşli","ılık","normal", "şiddetli","evet"],
        ["bulutlu","ılık","yüksek","şiddetli","evet"],
        ["bulutlu","sıcak","normal","zayıf","evet"],
        ["yağmurlu","ılık","yüksek","şiddetli","hayır"]]

sinifAdlari = ["Hava Durumu","Sıcaklık Derecesi","Nem Oranı",
                   "Rüzgar","Oynanma Durumu"]
siniflandirilacakOrnek = ["yağmurlu","sıcak","yüksek","zayıf"]

kararDegeri1 = "evet"
kararDegeri2 = "hayır"

def frekansiVeOlasiliklariYaz(k1,k2,sinifAdlari,frekansAd,f1,f2):
    frekansAdNoLastEleman = frekansAd.copy()
    frekansAdNoLastEleman.pop(-1)
    for i,ad in enumerate(frekansAdNoLastEleman):
        print("{:<25}{:<25}Olasılık".format(sinifAdlari[i],sinifAdlari[-1]))
        print("------------------------------------------------------------------")
        print("{:>29}{:>10}{:>18}{:>10}".format(k1,k2,"P("+k1+")","P("+k2+")"))
        print("------------------------------------------------------------------")
        for x,a in enumerate(ad):
            f01 = f1[sinifAdlari[i]][a]
            f02 = f2[sinifAdlari[i]][a]
            print("{:<25}{:<10}{:<15}{}/{:<6} {}/{}".format(a, f01, f02, f01, f01 + f02, f02, f01 + f02))
        print("\n")

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        try:
            num, denom = frac_str.split('/')
        except ValueError:
            return None
        try:
            leading, num = num.split(' ')
        except ValueError:
            return float(num) / float(denom)
        if float(leading) < 0:
            sign_mult = -1
        else:
            sign_mult = 1
        return float(leading) + sign_mult * (float(num) / float(denom))

def say(veri_t, frekansAd,e,k):
    toplam=0
    for i in range(len(veri_t[k])):
        if veri_t[k][i] == frekansAd and veri_t[-1][i] == e:
            toplam +=1
    return toplam
def frekansBul(frekansAd,sinifAdlari,veri_transpoze,k):
    frekans = {}
    for i, ad in enumerate(frekansAd):
        frekans[sinifAdlari[i]] = {}
        for a in ad:
            frekans[sinifAdlari[i]][a] = say(veri_transpoze, a, k, i)

    return frekans

def frekansOlasilikBul(f1,f2,frekansAd,sinifAdlari):
    frekansO = {}
    for i, ad in enumerate(frekansAd):
        frekansO[sinifAdlari[i]] = {}
        for a in ad:
            frekansO[sinifAdlari[i]][a] = Fraction(f1[sinifAdlari[i]][a], (f1[sinifAdlari[i]][a] + f2[sinifAdlari[i]][a]))
    return frekansO

def frekansAdiVeDegeri(k1,k2,veri,sinifAdlari):
    frekansAd = []
    veri_copy = veri.copy()
    veri_transpoze = list(map(list, zip(*veri_copy)))
    for x in veri_transpoze:
        frekansAd.append(list(set(x)))
    #print(frekansAd)
    #print(veri_transpoze)
    frekans1 = frekansBul(frekansAd, sinifAdlari, veri_transpoze, k1)
    frekans2 = frekansBul(frekansAd, sinifAdlari, veri_transpoze, k2)
    #print(frekans1)
    #print(frekans2)
    k1sayisi = frekans1[sinifAdlari[-1]][k1]
    k2sayisi = frekans2[sinifAdlari[-1]][k2]

    frekansiVeOlasiliklariYaz(k1,k2,sinifAdlari,frekansAd,frekans1,frekans2)
    frekansOlasilik1 = frekansOlasilikBul(frekans1,frekans2,frekansAd,sinifAdlari)
    frekansOlasilik2 = frekansOlasilikBul(frekans2,frekans1,frekansAd,sinifAdlari)
    return frekansOlasilik1, frekansOlasilik2, k1sayisi, k2sayisi

f1O ,f2O, k1s, k2s = frekansAdiVeDegeri(kararDegeri1,kararDegeri2,veri,sinifAdlari)
k1o = Fraction(k1s, (k1s + k2s))
k2o = Fraction(k2s, (k1s + k2s))

def P(fo, ornek, ko, sinifAd,k):
    PO = Fraction(1)
    print("p({}|x) = ".format(k),end="")
    for i,o in enumerate(ornek):

        PO *= fo[sinifAd[i]][o]
        print(fo[sinifAd[i]][o],"* ",end="")
    PO *= ko
    print(ko)
    return PO

k1olasilik = P(f1O,siniflandirilacakOrnek,k1o, sinifAdlari,kararDegeri1)

print("\t\t  =",k1olasilik)
float1 = round(convert_to_float(k1olasilik),4)
print("\t\t  =",float1,end="\n\n")
k2olasilik = P(f2O,siniflandirilacakOrnek,k2o, sinifAdlari,kararDegeri2)
float2 = round(convert_to_float(k2olasilik),4)
print("\t\t  =",float2,end="\n\n")

if float1 > float2:
    print("{} > {} olduğu için özellik \"{}\" olarak sınıflandırılır.".format(float1,float2,kararDegeri1))
else:
    print("{} > {} olduğu için özellik \"{}\" olarak sınıflandırılır.".format(float2, float1, kararDegeri2))