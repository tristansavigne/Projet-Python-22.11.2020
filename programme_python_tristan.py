import matplotlib.pyplot as plt
#matplo... c'est module qu'on a importer pour faire des graphique qu'on racourcit en pd
import pandas as pd
import datetime
from datetime import datetime as dt # ici il y a un module dans datetime qui se nomme datetime mais qui permet lui de transformer un mot (chaîne de caractère en date. Ici on l'appel 'dt' parce que sinon python ne serait jamais duquelles nous parlons.
import statistics as st


default_sd = dt.strptime('2018-01-01 00:00:00+02:00', '%Y-%m-%d %H:%M:%S%z')
default_ed = dt.strptime('2019-08-25 17:47:08+02:00', '%Y-%m-%d %H:%M:%S%z')
#sd on décide de mettre pour startdate (idem ed = enddate)
#le '=' en python permet de laisser le choix à l'utilisateur de mettre la date qu'il veut sinon c'est la date qu'on à mise qui sera prise
#dt.strptime('', '%Y-%m-%d %H:%M:%S%z') on a trouvé sur internet pour mettre la date et heure et le fuseau horaire

matrice = pd.read_csv('EIVP_KM.csv', sep = ';', header = None)


#csv = pd.read_csv('EIVP_KM.csv', sep = ';', header = None)
#longeur = len(csv[1]) # donner la longeur de la colonne 1. Pas possible longeur = len(csv[1][i]) car 1. ne sait pas ce que c'est 'i' et 2. ça va te donner juste une cellule.
#Le csv se lit comment une suite de 2 listes, colonne et ligne.
#for k in range (1,longeur):
    #csv[7][k] = dt.strptime(csv[7][k], '%Y-%m-%d %H:%M:%S%z')  #on veut défnir les cellules des dates comme des dates et non des suites de caractères (des mots). Car python si on lui dit pas va faire comme un mot.
#csv[7][0] = dt.strptime('2015-01-01 00:00:00+02:00', '%Y-%m-%d %H:%M:%S%z') # au lieu de la supprimer on la garde en mais on s'assure quelle sera en premier. Car se sont à l'origine pas des dates et donc pas comparable. Se sont des titres de colonnes.

#le shells n'est pas numéroter de la même façon que le python. Ca commence à 0.

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
    k = 2 #colonne 0, 1 , 2
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

#expliquer le 1

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

#expliquer le 2

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
    liste_abs = []
    j=1
    while dt.strptime(matrice[7][j], '%Y-%m-%d %H:%M:%S%z') < start_date :
        j = j + 1 # car i déjà utilisé,
    while dt.strptime(matrice[7][j], '%Y-%m-%d %H:%M:%S%z') < end_date :
        liste_abs.append(dt.strptime(matrice[7][j], '%Y-%m-%d %H:%M:%S%z')) # liste_ord supprimer car on enlève donnée (variable de l'algo 1) et on met humidex à la place.
        j = j + 1
    plt.plot(liste_abs, res) #abscisse et ordonnée
    plt.show()
    return res

dt.strptime('2019-08-25 11:45:54+02:00', '%Y-%m-%d %H:%M:%S%z')


#expliquer le 3

def programme_4( x, y, start_date = default_sd, end_date = default_ed) :
    k=2
    while x != matrice[k][0] :
        k = k+1
    h=2
    while y != matrice [h][0]:
        h=h+1
    listex = matrice [k][1:]
    listey = matrice [h][1:]
    espx = st.mean(listex)
    espy = st.mean(listey)
    sigmax = st.stdev(listex)
    sigmay = st.stdev(listey)
    n = len(listex)
    listexy = []
    for j in range(n):
       listexy.append(listex[j]*liste[j])
    espxy = st.mean(listexy)
    r = (espxy - espx*espy)/(sigmax*sigmay)
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
    plt.subplot(211) # 211 juste pour placer le graph en haut ou en bas.

    plt.plot(liste_abs, liste_ord1, label = x)  #mettre liste absisse puis ordonnée et après c'est pour assigner la valeur au graphique pour la légende.
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.title('r = ' + str(r))
    plt.subplot(212)
    plt.plot(liste_abs, liste_ord2, label = y)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.show()


