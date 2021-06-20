import math
"""
Vize Sorusu:

veriler = [[32,1,"F"],
           [40,1,"T"],
           [16,0,"K"],
           [34,0,"K"],
           [55,1,"T"],
           [40,1,"K"],
           [20,0,"T"],
           [15,1,"K"],
           [55,0,"F"],
           [15,1,"F"]]
istenen = [15,0]
k=3

"""
# NOT:
# Eğer 2 den fazla k değeri çeşiti yani k değerleri seçildikten sonra veriler[][3] değeri çeşiti 2 den fazlaysa
# algoritmanın son 2 satırlık açıklaması çalışmayacaktır.
# Yani sonuc() fonksiyonu çalışmayacaktır.

# Videodaki örnek soru:
# veriler tablodan diziye aşağıdaki gibi aktarılmalıdır.
veriler = [[158,58,"M"],
           [158,59,"M"],
           [158,63,"M"],
           [160,59,"M"],
           [160,60,"M"],
           [163,60,"M"],
           [163,61,"M"],
           [160,64,"L"],
           [163,64,"L"],
           [165,61,"L"],
           [165,62,"L"],
           [165,65,"L"],
           [168,62,"L"],
           [168,63,"L"],
           [168,66,"L"],
           [170,63,"L"],
           [170,64,"L"],
           [170,68,"L"]]

istenen = [161,61] # istenen değere ait özellikler bu değişkene girilir.

k = 5 # k değeri bu değişkene girilir.


def oklid( eski_veriler , i):
    print("\n------------------------------------------------")
    print("ÖKLİD UZAKLIĞI HESABI:")
    print("------------------------------------------------")
    print("formül: [(x2 - x1)^2 + (y2 - y1)^2]^(1/2)")
    veriler = eski_veriler.copy()
    for v in veriler:
        print("\n[{}, {}] noktasına olan öklid uzaklığı hesabı: \n".format(v[0],v[1]))
        uzaklik = round(math.sqrt(((int(i[0]) - int(v[0])) ** 2) + ((int(i[1]) - int(v[1])) ** 2)),3)
        print("= [({} - {})^2 + ({} - {})^2]^(1/2)".format(i[0],v[0],i[1],v[1]))
        print("= [({})^2 + ({})^2]^(1/2)".format(i[0] - v[0],i[1] - v[1]))
        print("= ({} + {})^(1/2)".format((i[0] - v[0])**2, (i[1] - v[1])**2))
        print("= ({})^(1/2)".format((i[0] - v[0]) ** 2 + (i[1] - v[1]) ** 2))
        print("= {}".format(uzaklik))
        v.append(uzaklik)
    return veriler

yeniVeriler = oklid(veriler,istenen)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # veri listemiz 3 boyutlu olduğu için sıralama algoritmasındaki kod değişikliği
            if arr[j][3] > arr[j + 1][3]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def kDegerleriniBul(eski_veriler,k):
    veriler = eski_veriler.copy()
    # Verilerin orjinal sıralarını belirliyoruz.
    for i, v in enumerate(veriler):
        v.append(i)
    # Verileri öklid uzaklıklarına göre sıralıyoruz.
    siraliVeriler = bubbleSort(veriler)
    # k değerine göre en küçük değerleri alıyoruz.
    kDegerleri = siraliVeriler[0:k]
    return kDegerleri

def kDegerleriniEkle(veriler,kDegerleri,K):
    for i,v in enumerate(veriler):
        v.append(0)
    for i,k in enumerate(kDegerleri):
        veriler[k[4]][5] = i+1
    print("\nHesaplar tamamlandıktan sonra k={} olduğundan dolayı en küçük değerden başlayarak {} değer alınır.\n"
          .format(K,K))
    print("\tx\t\ty\t\tf(x,y)\t\tÖklid\t\tk")
    print("  ---------------------------------------------")
    for i,v in enumerate(veriler):
        if v[5] != 0 :
            print("\t{}\t\t{}\t\t{}\t\t\t{}\t\t{}*".format(v[0], v[1], v[2], v[3], v[5]))
        else:
            print("\t{}\t\t{}\t\t{}\t\t\t{}".format(v[0], v[1], v[2], v[3]))
kDegerleri = kDegerleriniBul(veriler,k)
kDegerleriniEkle(veriler,kDegerleri,k)

def sonuc(kDegerleri):
    k = kDegerleri.copy()
    kd = list(map(list, zip(*kDegerleri)))
    setf = list(set(kd[2]))
    sonuc = [[],[]]
    for i,f in enumerate(setf):
        sonuc[i].append(f)
        sonuc[i].append(kd[2].count(f))
    print("\nEn yakın komşuların {} tanesi {} ve {} tanesi {} olarak tespit edilmiştir.\n"
          .format(sonuc[0][1],sonuc[0][0],sonuc[1][1],sonuc[1][0]))
    if sonuc[0][1] > sonuc[1][1]:
        print("{} > {} olduğundan sonuç {} diyebiliriz.\n".format(sonuc[0][1],sonuc[1][1],sonuc[0][0]))
    else:
        print("{} > {} olduğundan sonuç {} diyebiliriz.\n".format(sonuc[1][1],sonuc[0][1],sonuc[1][0]))

try:
    sonuc(kDegerleri)
except:
    print("\nSeçilen k değer çeşiti 2 den fazla olduğu için algoritmanın bulduğu çözüm buraya kadardır.")
