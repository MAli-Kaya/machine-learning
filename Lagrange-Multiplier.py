
from sympy import *

"""
f = (x**2 + 1) / (x - 1)

print(f.subs(x,2))

pprint(1 + sqrt(2))
pprint(Integral(sqrt(1/x) + exp(x),x))

print_latex(Integral(sqrt(1/x) + exp(x),x))

f = sin(x)**2 + cos(x)**2
pprint(f)
print_latex(f)

f = x**2 - 2*x + y**2 - y + 1.25
g = x**2 + y**2 - 5 """
x, y, λ = symbols("x y λ")
f = x**2 + 4*y**2 - 2*x + 8*y
g = x + 2*y - 7

def lagrangeFonk(f,g):
    #L0 = f - λ * g
    L = (f - λ * g).expand()
    print("\nLagrange Formülü:\nL = f(x,y) + λ*g(x,y)\n")
    print("Lagrange Denklemi:")
    pprint(L)
    print("")
    # pprint(collect(L.expand(),x))
    # pprint(simplify(L))
    print("")
    # pprint(L.factor())
    return L

L = lagrangeFonk(f,g)

def turev(L, a):
    La = diff(L,a)
    print("L'nin {}'e göre türevi:\nL{}(x, y, λ) = ".format(a,a),end="")
    pprint(La)
    return La

def denklemYaz(L,a):
    print("ise {} = ".format(a))
    eqx = solveset(Eq(L, 0), a)
    pprint(eqx)
    print("")


def optimumNokta(x, y, λ, L):
    # x için türev
    Lx = turev(L,x)
    denklemYaz(Lx,x)
    # y için türev
    Ly = turev(L, y)
    denklemYaz(Ly, y)
    # λ için türev
    Lλ = turev(L, λ)
    # x, y ve λ nın çözümü
    liste = list(linsolve([Lx, Ly, Lλ], (x, y, λ)))
    # sonuçları sembolden integer değere çevirme
    x1 = liste[0][0]
    y1 = liste[0][1]
    # x ve y değerlerini ve optimum noktayı yazdırma
    pprint("\nise x = {}, y = {} olarak bulunur.".format(x1, y1))
    print("\nBuradan F(x,y) için optimum nokta ({}, {}) olur.".format(x1, y1))

    return x1,y1

opNokta = optimumNokta(x, y, λ, L)

x1 = opNokta[0]
x2 = opNokta[1]

def sonuc(x1, y1, x, y,f):
    # foksiyon değerinin adım adım yazdırılması
    print("\nF({}, {}) fonksiyonunun hesabı:".format(x1, y1), )
    # 1. adım fonksiyonun kendisi
    pprint(f)
    # önce değişkenleri string e çevirmeliyiz ki fonksiyonu manipüle edebilelim
    strf = str(f)
    strX = str(x1)
    strY = str(y1)
    strX = "(" + strX + ")"
    strY = "(" + strY + ")"
    # 2. adım optimum nokta değerlerinin fonksiyonda yerine konması
    strf = strf.replace("x", strX)
    strf = strf.replace("y", strY)
    strf = strf.replace("**", "^")
    print("\n= {}\n".format(strf))
    # 3. adım sonucu yazdırma
    print("=",f.subs(x, x1).subs(y, y1))

FoksiyonDeğeri = sonuc(x1, x2, x, y, f)
