import matplotlib.pyplot as plt
import pandas as pd
import datetime
from datetime import datetime as dt
import statistics as st

default_sd = dt.strptime('2018-01-01 00:00:00+02:00', '%Y-%m-%d %H:%M:%S%z')
default_ed = dt.strptime('2019-08-25 11:45:54+02:00', '%Y-%m-%d %H:%M:%S%z')

def programme_1(x, start_date = default_sd, end_date = default_ed) :
    liste_abs = []
    liste_ord = []
    matrice = pd.read_csv('EIVP_KM.csv', sep = ';', header = None)
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
    matrice = pd.read_csv('EIVP_KM.csv', sep = ';', header = None)
    k = 2
    while x != matrice[k][0] :
        k = k + 1
    i = 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < start_date :
        i = i + 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < end_date :
        liste.append(float(matrice[k][i]))
        i = i + 1
    m = min(liste)
    M = max(liste)
    sigma = st.stdev(liste)
    moy = st.mean(liste)
    var = st.variance(liste)
    med = st.median(liste)
    return('min =', m, 'max =', M, 'ecart type =', sigma, 'moyenne =', moy, 'variance =', var, 'mediane =', med)

def programme_3(start_date = default_sd, end_date = default_ed) :
    res = []
    liste_1 = []
    liste_2 = []
    matrice = pd.read_csv('EIVP_KM.csv', sep = ';', header = None)
    i = 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < start_date :
        i = i + 1
    while dt.strptime(matrice[7][i], '%Y-%m-%d %H:%M:%S%z') < end_date :
        liste_1.append(float(matrice[3][i]))
        liste_2.append(float(matrice[4][i]))
        i = i + 1
    n = len(liste_1)
    for k in range(n) :
        res.append(liste_1[k] + (5/9) *(6.112 * (10**((7.5*liste_1[k])/(237.7 + liste_1[k])))*(liste_2[k]/100) - 10))
    return res

def programme_4(start_date = default_sd, end_date = default_ed, x, y) :
    matrice = pd.read_csv('EIVP_KM.csv', sep = ';', header = None)
    k = 2
    while x != matrice[k][0] :
        k = k + 1
    h = 2
    while y != matrice[h][0] :
        h = h + 1
    listex = matrice[k][1:]
    listey = matrice[h][1:]
    espx = st.mean(listex)
    espy = st.mean(listey)
    sigx = st.stdev(listex)
    sigy = st.stdev(listey)
    n = len(listex)
    listexy = []
    for i in range(n) :
        listexy.append(listex[i] * listey[i])
    espxy = st.mean(listexy)
    r = (espxy - espx * espy) / (sigx * sigy)





dt.strptime('2019-08-25 11:45:54+02:00', '%Y-%m-%d %H:%M:%S%z')
