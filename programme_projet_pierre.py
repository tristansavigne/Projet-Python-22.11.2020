import matplotlib.pyplot as plt
import pandas as pd
import datetime
from datetime import datetime as dt
import statistics as st
import matplotlib.dates as md

default_sd = dt.strptime('2018-01-01 00:00:00+02:00', '%Y-%m-%d %H:%M:%S%z')
default_ed = dt.strptime('2019-08-25 17:47:08+02:00', '%Y-%m-%d %H:%M:%S%z')
default_ed2 = dt.strptime('2019-08-25 17:32:08+02:00', '%Y-%m-%d %H:%M:%S%z')

matrice = pd.read_csv('EIVP_KM.csv', sep = ';', header = None)

#csv = pd.read_csv('EIVP_KM.csv', sep = ';', header = None)
#longueur = len(csv[1])
#for k in range(1, longueur) :
    #csv[7][k] = dt.strptime(csv[7][k], '%Y-%m-%d %H:%M:%S%z')
#csv[7][0] = dt.strptime('2015-01-01 00:00:00+02:00', '%Y-%m-%d %H:%M:%S%z')

#def tri(t) :
    #n = len(t[1])
    #for i in range(n) :
        #for k in range(n - i - 1) :
            #if t[7][k] > t[7][k + 1] :
                #for y in range(8) :
                    #t[y][k], t[y][k+1] = t[y][k+1], t[y][k]




def programme_1(x, start_date = default_sd, end_date = default_ed) :
    liste_abs = []
    liste_ord = []
    k = 2
    while x != matrice[k][0] :
        k = k + 1
    i = 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < start_date :
        i = i + 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < end_date :
        liste_abs.append(dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z'))
        liste_ord.append(float(matrice[k][i]))
        i = i + 1
    plt.plot(liste_abs, liste_ord)
    plt.show()


def programme_2(x, start_date = default_sd, end_date = default_ed) :
    liste = []
    liste_abs = []
    liste_ord = []
    k = 2
    while x != matrice[k][0] :
        k = k + 1
    i = 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < start_date :
        i = i + 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < end_date :
        liste.append(float(matrice[k][i]))
        liste_abs.append(dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z'))
        liste_ord.append(float(matrice[k][i]))
        i = i + 1
    m = min(liste)
    M = max(liste)
    sigma = st.stdev(liste)
    moy = st.mean(liste)
    var = st.variance(liste)
    med = st.median(liste)
    plt.plot(liste_abs, liste_ord)
    txt = 'min =' + str(m) + ';' + 'max =' + str(M) + ';' + 'ecart type =' + str(sigma) + ';' + 'moyenne =' + str(moy) + ';' + 'variance =' + str(var) + ';' + 'mediane =' + str(med)
    plt.title(txt)
    plt.show()

def programme_3(start_date = default_sd, end_date = default_ed) :
    res = []
    liste_1 = []
    liste_2 = []
    i = 1
    liste_abs = []
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < start_date :
        i = i + 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < end_date :
        liste_abs.append(dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z'))
        liste_1.append(float(matrice[3][i]))
        liste_2.append(float(matrice[4][i]))
        i = i + 1
    n = len(liste_1)
    for k in range(n) :
        res.append(liste_1[k] + (5/9) *(6.112 * (10**((7.5*liste_1[k])/(237.7 + liste_1[k])))*(liste_2[k]/100) - 10))
    plt.plot(liste_abs, res)
    plt.show()
    return res

def programme_4(x, y, start_date = default_sd, end_date = default_ed) :
    k = 2
    while x != matrice[k][0] :
        k = k + 1
    h = 2
    while y != matrice[h][0] :
        h = h + 1
    listex = [float(matrice[k][i]) for i in range(1, len(matrice[2]))]
    listey = [float(matrice[h][i]) for i in range(1, len(matrice[2]))]
    espx = st.mean(listex)
    espy = st.mean(listey)
    sigx = st.stdev(listex)
    sigy = st.stdev(listey)
    n = len(listex)
    listexy = []
    for j in range(n) :
        listexy.append(listex[j] * listey[j])
    espxy = st.mean(listexy)
    r = (espxy - espx * espy) / (sigx * sigy)
    liste_abs = []
    liste_ord1 = []
    liste_ord2 = []
    i = 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < start_date :
        i = i + 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < end_date :
        liste_abs.append(dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z'))
        liste_ord1.append(float(matrice[k][i]))
        liste_ord2.append(float(matrice[h][i]))
        i = i + 1
    plt.subplot(211)
    plt.plot(liste_abs, liste_ord1, label = x)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.title('r = ' + str(r))
    plt.subplot(212)
    plt.plot(liste_abs, liste_ord2, label = y)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.show()

def MONSCRIPT(action, x = 'temp', y = 'humidity', start_date = default_sd, end_date = default_ed) :
    if action == 'display' :
        if x == 'humidex' :
            programme_3(start_date, end_date)
        else :
            programme_1(x, start_date, end_date)
    if action == 'displayStat' :
        programme_2(x, start_date, end_date)
    if action == 'correlation' :
        programme_4(x, y, start_date, end_date)
    else :
        return('probleme ecriture action')

#on remarque dans les données que la lumière des bureau s'allume aux allentours de 7h45 tous les matins et s'éteint vers 20h40 le soir. Cependant, il peut arriver qu'il y ait de la lumière détectée entre 20h40 et 7h45 sans pour autant que ce soit une erreur (sûrement de la lumière issue de l'extérieur) : captation de lumière faible (< 10) et non régulière. Considérons qu'il y a une erreur pour toute captation > 30 et pour toute captation de lumière sur 3 échantillon de suite entre 22h et 7h (si on prend en compte les gens qui peuvent arriver plus tôt ou repartir plus tard). Pour un soucis de lisibilité, on ne montrera qu'une erreur par jour si il y en a.

def erreur_lum() :
    liste_erreurs = []
    liste_jours_concernes : []
    i = 1
    jour = 11
    drap = True
    while jour < 25 :
        while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z').hour < 22 :
            i = i + 1
        while 22 <= dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z').hour <= 23 and drap == True:
            if float(matrice[5][i]) > 30 :
                liste_erreurs.append((jour,i))
                drap = False
                i = i + 1
            elif float(matrice[5][i]) > 0 and float(matrice[5][i+1]) > 0 and float(matrice[5][i+2]) > 0 :
                liste_erreurs.append((jour, i))
                drap = False
                i = i + 3
            else :
                i = i + 1
        while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z').hour < 7 and drap == True :
            if float(matrice[5][i]) > 30 :
                liste_erreurs.append((jour,i))
                drap = False
                i = i + 1
            elif float(matrice[5][i]) > 0 and float(matrice[5][i+1]) > 0 and float(matrice[5][i+2]) > 0 :
                liste_erreurs.append((jour, i))
                drap = False
                i = i + 3
            else :
                i = i + 1
        while not 7 < dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z').hour < 22 :
            i = i + 1
        jour = jour + 1
        drap = True
    liste_abs = []
    liste_ord = []
    i = 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < default_ed :
        liste_abs.append(dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z'))
        liste_ord.append(float(matrice[5][i]))
        i = i + 1
    n = len(liste_erreurs)
    plt.plot(liste_abs, liste_ord)
    ax = plt.axes()
    for h in range(n) :
        x0 = md.date2num(dt.strptime(matrice[7][liste_erreurs[h][1]], '%Y-%m-%d %H:%M:%S%z') + datetime.timedelta(days = -3))
        y0 = 1400
        dx = md.date2num(dt.strptime(matrice[7][liste_erreurs[h][1]], '%Y-%m-%d %H:%M:%S%z')) - x0
        dy = float(matrice[5][liste_erreurs[h][0]]) - 1400
        ax.arrow(x0, y0, dx, dy, head_width=0.5, head_length=70, zorder = 2, fc='black', ec='black')
    plt.title('les fleches indiquent la presence anormale declairage la nuit')
    plt.show()

#Normalement, l'humidité relative et la température ont un comportement miroir, c'est a dire h augmente quand t décroit et réciproquement. Cependant, on observe dans les données qu'il y a une zone ou cela n'est pas vérifié. Le but est de faire un programme capable de déceler ces zones. On choisit de relever comme erreur tous les points tels que humlidity et temp ont des sens de variation identiques deux fois de suite.

def erreur_humidity() :
    i = 1
    liste_erreurs = []
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < default_ed2  :
        if float(matrice[3][i]) - float(matrice[3][i + 1]) < 0 and float(matrice[4][i]) - float(matrice[4][i + 1]) < 0 :
            if float(matrice[3][i + 1]) - float(matrice[3][i + 2]) > 0 and float(matrice[4][i + 1]) - float(matrice[4][i + 2]) > 0 :
                liste_erreurs.append((i, dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z').day))
        if float(matrice[3][i]) - float(matrice[3][i + 1]) < 0 and float(matrice[4][i]) - float(matrice[4][i + 1]) < 0 :
            if float(matrice[3][i + 1]) - float(matrice[3][i + 2]) < 0 and float(matrice[4][i + 1]) - float(matrice[4][i + 2]) < 0 :
                liste_erreurs.append((i, dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z').day))
        if float(matrice[3][i]) - float(matrice[3][i + 1]) > 0 and float(matrice[4][i]) - float(matrice[4][i + 1]) > 0 :
            if float(matrice[3][i + 1]) - float(matrice[3][i + 2]) > 0 and float(matrice[4][i + 1]) - float(matrice[4][i + 2]) > 0 :
                liste_erreurs.append((i, dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z').day))
        if float(matrice[3][i]) - float(matrice[3][i + 1]) > 0 and float(matrice[4][i]) - float(matrice[4][i + 1]) > 0 :
            if float(matrice[3][i + 1]) - float(matrice[3][i + 2]) < 0 and float(matrice[4][i + 1]) - float(matrice[4][i + 2]) < 0 :
                liste_erreurs.append((i, dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z').day))
        i = i + 1
    liste_abs = []
    liste_ord = []
    i = 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < default_ed :
        liste_abs.append(dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z'))
        liste_ord.append(float(matrice[4][i]))
        i = i + 1
    n = len(liste_erreurs)
    plt.plot(liste_abs, liste_ord)
    ax = plt.axes()
    for h in range(n) :
        x0 = md.date2num(dt.strptime(matrice[7][liste_erreurs[h][0]], '%Y-%m-%d %H:%M:%S%z'))
        y0 = 30
        dx = 0
        dy = float(matrice[4][liste_erreurs[h][0]]) - 30
        ax.arrow(x0, y0, dx, dy, head_width=0.4, head_length=2, zorder = 2, fc='black', ec='black')
    plt.title('les fleches indiquent des variations de humidity en desaccord avec les variations de temp')
    plt.show()

#D'après l'étude graphique, on constate que le quantité de co2 est anormalement élevé certains jours. D'après les données, on considère qu'au dessus de 650 ptm, la quantité de co2 est anormale.

def erreur_co2() :
    liste_erreurs = []
    i = 1
    jour = 11
    drap = True
    while jour <= 25 :
        while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < default_ed and drap == True :
            if float(matrice[6][i]) > 650 :
                liste_erreurs.append(i)
                drap = False
            i = i + 1
        while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z').day != jour + 1 and dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < default_ed :
            i = i + 1
        jour = jour + 1
        drap = True
    liste_abs = []
    liste_ord = []
    i = 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < default_ed :
        liste_abs.append(dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z'))
        liste_ord.append(float(matrice[6][i]))
        i = i + 1
    n = len(liste_erreurs)
    plt.plot(liste_abs, liste_ord)
    ax = plt.axes()
    for h in range(n) :
        x0 = md.date2num(dt.strptime(matrice[7][liste_erreurs[h]], '%Y-%m-%d %H:%M:%S%z'))
        y0 = 800
        dx = 0
        dy = float(matrice[6][liste_erreurs[h]]) - 800
        ax.arrow(x0, y0, dx, dy, head_width=0.3, head_length=20, zorder = 2, fc='black', ec='black')
    plt.title('les fleches indiquent des pics de co2 anormaux')
    plt.show()





















