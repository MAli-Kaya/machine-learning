
KarMatrix = [[965,20],
             [10,5]]

DP = KarMatrix[0][0]
YP = KarMatrix[0][1]
YN = KarMatrix[1][0]
DN = KarMatrix[1][1]

def DPOrani(matrix):
    DP = round(matrix[0][0] / (matrix[0][0] + matrix[1][0]),4)
    print("\nDOĞRU POZİTİF ORANI:")
    print("DPOranı = DP / (DP + YN)")
    print("        = {} / ({} + {})".format(matrix[0][0],matrix[0][0],matrix[1][0]))
    print("        = {} / {}".format(matrix[0][0],matrix[0][0] + matrix[1][0]))
    print("DPOranı = {}".format(DP))
    return DP

DPOrani = DPOrani(KarMatrix)

def YPOrani(matrix):
    YP = round(matrix[0][1] / (matrix[0][1] + matrix[1][1]), 4)
    print("\nYANLIŞ POZİTİF ORANI:")
    print("YPOranı = YP / (YP + DN)")
    print("        = {} / ({} + {})".format(matrix[0][1], matrix[0][1], matrix[1][1]))
    print("        = {} / {}".format(matrix[0][1], matrix[0][1] + matrix[1][1]))
    print("YPOranı = {}".format(YP))
    return YP

YPOrani = YPOrani(KarMatrix)

def dogrulukHesapla(DP, YP, YN, DN):
    dogruluk = round((DP + DN)/(DP + YP + DN + YN),3)
    print("\nDOĞRULUK HESABI:")
    print("Doğruluk = (DP + DN)/(DP + YP + DN + YN)")
    print("         = ({} + {}) / ({} + {} + {} + {})".format(DP,DN,DP,YN,YP,DN,YN))
    print("         = {} / {}".format(DP + DN,DP + YN + YP + DN + YN))
    print("Doğruluk = {}".format(dogruluk))
    return dogruluk

Doğruluk = dogrulukHesapla(DP, YP, YN, DN)

def kesinlikHesapla(DP, YP):
    kesinlik = round(DP / (DP + YP),3)
    print("\nKESİNLİK HESABI:")
    print("Kesinlik = DP / (DP + YP)")
    print("         = ({} / ({} + {})".format(DP, DP, YP))
    print("         = {} / {}".format(DP, DP + YP))
    print("Kesinlik = {}".format(kesinlik))
    return kesinlik

K = kesinlikHesapla(DP,YP)

def hassasiyetHesapla(DP, YN):
    hassasiyet = round(DP / (DP + YN),3)
    print("\nHASSASİYET HESABI:")
    print("Hassasiyet = DP / (DP + YN)")
    print("           = ({} / ({} + {})".format(DP, DP, YN))
    print("           = {} / {}".format(DP, DP + YN))
    print("Hassasiyet = {}".format(hassasiyet))
    return hassasiyet

H = hassasiyetHesapla(DP,YN)

def F_OlcutuHesapla(K, H):
    F_Olcutu = round(2*(K * H) / (K + H),3)
    print("\nHASSASİYET HESABI:")
    print("F-Ölçütü = 2 x [(K x H) / (K + H)]")
    print("         = 2 x [({} x {}) / ({} + {})]".format(K, H, K, H))
    print("         = {} / {}".format(2 * K * H, K + H))
    print("F-Ölçütü = {}".format(F_Olcutu))
    return F_Olcutu

Fm = F_OlcutuHesapla(K, H)