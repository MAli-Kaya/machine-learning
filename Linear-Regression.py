# vize sorusu
# dizi = [[100,110], [110,130], [140,150], [150,160], [200,180]]
# x= 175 (istenen değeri unuttum)

# ders videosundaki örnek soru
dizi = [[2,4], [3,5], [5,7], [7,10], [9,15]] # verilen x ve y değerleri format: [[x1,y1],[x2,y2],...,[xn,yn]]
x = 8 # istenen değer

def toplama(dizi):
    toplam = [0,0,0,0]
    for eleman in dizi:
        for count, x in enumerate(eleman):
            toplam[count] += x
    return toplam

def carpma(dizi):
    for eleman in dizi:
        eleman.append(round(eleman[0] **2, 4))
        eleman.append(round(eleman[0] * eleman[1],4))
    return dizi


def yazdirToplam(carp, top):
    print("\nX^2 VE X*Y İLE TOPLAMLARIN HESABI:")
    print("----------------------------------\n")
    print("   X         Y            X^2           X*Y")
    for eleman in carp:
        print("  {}          {}            {}            {}".format(eleman[0],eleman[1],eleman[2],eleman[3]))
    print("+......   +.......      +......      +.......")
    print("  {}         {}            {}           {}".format(top[0], top[1], top[2], top[3]))

def egim(N, toplam):
    m = round(((N*toplam[3]) - (toplam[0]*toplam[1])) / ((N*toplam[2]) - (toplam[0])**2),4)
    print("\n\nEĞİM HESABI:")
    print("-------------------------------------")
    print("\n m = ( {} x {} - {} x {} ) / ( {} x {} - {}^2 )".format(N,toplam[3],toplam[0],toplam[1],N,toplam[2],toplam[0]))
    print("\n m = ( {} - {} ) / ( {} - {} )".format(N * toplam[3], toplam[0] * toplam[1], N * toplam[2], toplam[0]**2))
    print("\n m = ( {} ) / ( {} )".format(N * toplam[3] - toplam[0] * toplam[1], N * toplam[2] - toplam[0] ** 2))
    print("\n m = ",m)
    return m

def kesisim(N, m, toplam):
    b = round((toplam[1] - m*toplam[0])/N,4)
    print("\n\nKESİŞİM HESABI:")
    print("-------------------------------------")
    print("\n b = ( {} - {} x {} ) / {}".format(toplam[1],m,toplam[0],N))
    print("\n b = ( {} - {} ) / {}".format(toplam[1], m * toplam[0], N))
    print("\n b = {} / {}".format(round(toplam[1] - m * toplam[0],4), N))
    print("\n b = ", b)
    return b

def hatalar(m, b, dizi):
    for nokta in dizi:
        y = round(m * nokta[0] + b,4)
        nokta.append(y)
        nokta.append(round(y - nokta[0],4))
    return dizi

def yazdirHatalar(dizi):
    print("\n\nHATA HESABI:")
    print("----------------------------------\n")
    print("  X       Y           y={}x+{}              Hata".format(m,b))
    for eleman in dizi:
        print("  {}       {}              {}                     {}".format(eleman[0],eleman[1],eleman[4],eleman[5]))


def denklemHesabi(m, b, x):
    y = round(m * x + b,4)
    print("\n\nİSTENEN X DEĞERİ HESABI:")
    print("-------------------------------------")
    print("\n y = mx + b")
    print("\n m = {}, b ={} ise denklem: y = {}x + {} olur.".format(m,b,m,b))
    print("\n x = {} için;".format(x))
    print("\n y = {}{} + {}".format(m,x,b))
    print("\n y = {} + {}".format(round(m * x,4), b))
    print("\n y = {} ".format(y))

N = len(dizi)
carpilmis = carpma(dizi)
toplanmis = toplama(carpilmis)
yazdirToplam(carpilmis, toplanmis)

m = egim(N, toplanmis)
b = kesisim(N,m,toplanmis)

denklemHesabi(m, b, x)

hataliDizi = hatalar(m, b, dizi)
yazdirHatalar(hataliDizi)

