import matplotlib.pyplot as plt
import pandas as pd
import datetime
default_sd = datetime.datetime(2018, 1, 1, 0, 0, 0)
default_ed = datetime.datetime(2021, 1, 1, 0, 0, 0)

def programme_1(x, start_date = default_sd.isoformat(' '), end_date = default_ed.isoformat(' ')) :
    liste_abs = []
    liste_ord = []
    matrice = pd.read_csv('EIVP_KM.csv', sep = ';', header = None)



datetime.strptime('2019-08-25 11:45:54+02:00', '%y-%m-%d %H-%M-%S')

