import math

def truncate(n):
    return int(n * 100) / 100

noktalar = [[2,10], [2,5], [8,4], [5,8], [7,5], [6,4], [1,2], [4,9]]
merkezler = [[2,10], [5,8], [1,2]]

#noktalar = [[-4,-3], [6,5], [1,-7], [-4,-6],[4,6],[-1,-5],[-3,0],[3,0]]
#merkezler = [[-3,0],[3,0]]

def Oklid( MS , NS):
    toplamUzakliklar = []
    print("\n------------------------------------------------")
    print("ÖKLİD UZAKLIĞI HEABI:")
    print("------------------------------------------------")
    for n1 in MS:
        print("\n", n1, 'Merkezi için öklid uzaklık hesabı: \n')
        uzakliklar = []
        i = 0
        for n2 in NS:
            i+=1
            uzaklik = truncate(math.sqrt(((int(n2[0]) - int(n1[0])) ** 2) + ((int(n2[1]) - int(n1[1])) ** 2)))
            print(i, ". Nokta için: [ (", end="")
            print("(", n2[0], ")",end="",sep="") if n2[0] <0 else print(n2[0],end="")
            print(" - ", end="")
            print("(", n1[0], ")",end="",sep="") if n1[0] <0 else print(n1[0],end="")
            print(')^2  + (',end="")
            print("(", n2[1], ")",end="", sep="") if n2[1] <0 else print(n2[1],end="")
            print(' - ',end="")
            print("(", n1[1], ")",end="", sep="") if n1[1] <0 else print(n1[1],end="",)
            print(')^2  ]^1/2 =', uzaklik, sep="")
            uzakliklar.append(uzaklik)

        toplamUzakliklar.append(uzakliklar)
    return toplamUzakliklar

def Kumeleme(OU):
    print("\n------------------------------------------------")
    print("NOKTALARIN AİT OLDUĞU KÜMELER")
    print("------------------------------------------------\n")
    print(" Nokta        Küme")
    print("-------      -------")
    Kumeler = []
    FlipOU = zip(*OU)
    for count, N in enumerate(FlipOU):
        kume = N.index(min(N))
        Kumeler.append(kume)
        print("  ", count+1, "          ", kume+1)
    return Kumeler

Kumeler = Kumeleme(Oklid(merkezler,noktalar))

def Merkez(Kumeler, noktalar):
    print("\n------------------------------------------------")
    print("MERKERLERİN KOORDİNAT HESABI")
    print("------------------------------------------------\n")
    Merkezler = [[0,0] for _ in range(len(set(Kumeler)))]
    for count, n in enumerate(noktalar):
        Merkezler[Kumeler[count]][0] += n[0]
        Merkezler[Kumeler[count]][1] += n[1]

    for count, m in enumerate(Merkezler):
        m[0] = m[0] / Kumeler.count(count)
        m[1] = m[1] / Kumeler.count(count)
    return Merkezler

Merkezler = Merkez(Kumeler, noktalar)

def printMerkez(Kumeler, noktalar, Merkezler):
    yaziSirasi = [[] for _ in range(len(set(Kumeler)))]
    for count1, y in enumerate(Kumeler):
        for count2, n in enumerate(noktalar):
            if count1 == count2:
                yaziSirasi[y].append(n)

    for c1, y in enumerate(yaziSirasi):
        print("Merkez", c1 + 1, " hesabı:", sep="")
        if len(y) == 1:
            print("=>", Merkezler[c1],"\n")
        else:
            print("=> [(", end='')
            for c2, m in enumerate(y):
                if c2 == 0:
                    print("(", m[0],")", end="", sep="") if m[0] < 0 else print(m[0], end="")
                else:
                    print(" + (",m[0],")", end="", sep="") if m[0] < 0 else print(" +", m[0], end="")
            print("),(", end="")

            for c2, m in enumerate(y):
                if c2 == 0:
                    print("(", m[1],")", end="", sep="") if m[1] < 0 else print(m[1], end="")
                else:
                    print(" + (",m[1],")", end="", sep="") if m[1] < 0 else print(" +", m[1], end="")
            print(")]")
            print("=>", Merkezler[c1],"\n")

printMerkez(Kumeler,noktalar,Merkezler)