import numpy as np
import matplotlib.pyplot as plt

def konvolusyon():
    xadet = int(input("Kaç adet x[k] değeri gireceksiniz ? : "))
    xList = list()
    xk = int(input("x[k] grafiğinin ilk k değerini giriniz : "))

    hadet = int(input("Kaç adet h[k] değeri gireceksiniz ? : "))
    hList = list()
    hk = int(input("h[k] grafiğinin ilk değerini giriniz : "))

    for i in range(xk, xadet+xk):
        xList.append(int(input("x[{}] değerini giriniz : ".format(i))))

    for i in range(hk, hadet+hk):
        hList.append(int(input("h[{}] değerini giriniz : ".format(i))))

    konv = np.zeros((xadet+1, xadet+hadet-1), dtype=int)

    #Bu döngü tablonun en üst değerlerini, oluşacak olan y[k] grafiğinin k değerlerini tutar
    for i in range(xadet+hadet-1):
        konv[0][i] = xk
        xk += 1

    #Bu döngü x[k] ve h[k] grafiğinin değerlerini çarpıp tabloda tutar
    for i in range(1, xadet+1):
        k = 0
        for j in range(i-1, xadet+hadet-1):
            konv[i][j] = xList[i-1] * hList[k]
            k += 1
            if k == hadet:
                break

    ########################----- ÇİZİM VE TOPLAMA İŞLEMLERİ -----########################

    #X ekseni değerlerini grafik için listeye  atama
    xEkseni = list()
    for i in range(xadet+hadet-1):
        xEkseni.append(konv[0][i])

    #Y ekseni değerlerini bulma
    yEkseni = list()
    for j in range(xadet+hadet-1):  #Sütun
        toplam = 0
        for i in range(1, xadet+1):  #Satır
            toplam += konv[i][j]
        yEkseni.append(toplam)

    print(xEkseni)
    print(yEkseni)
    plt.plot(xEkseni, yEkseni, 'ro')
    plt.show()

if __name__ == '__main__':
    konvolusyon()