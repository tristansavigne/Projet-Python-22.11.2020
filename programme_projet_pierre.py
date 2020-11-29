import matplotlib.pyplot as plt
import pandas as pd
import datetime
from datetime import datetime as dt
import statistics as st

default_sd = dt.strptime('2018-01-01 00:00:00+02:00', '%Y-%m-%d %H:%M:%S%z')
default_ed = dt.strptime('2019-08-25 17:47:08+02:00', '%Y-%m-%d %H:%M:%S%z')

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


dt.strptime('2019-08-25 11:45:54+02:00', '%Y-%m-%d %H:%M:%S%z')
