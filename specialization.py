import numpy as np
import csv

################# FONCTIONS D'INITIALISATION DE SPÉ #################

class spe:  #classe
    def __init__(self, x, pdps, cdps, pdmg, cdmg, color, name, seuil=["",0,1,""]):
        self.x=x
        self.pdps=pdps
        self.cdps=cdps
        self.pdmg=pdmg
        self.cdmg=cdmg
        self.color=color
        self.seuil=seuil
        self.name=name

def get_spe(name):	#lecture des .csv
    with open('specializations/'+name+'.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        data = np.array(data[1:]).astype(np.float64)
        pdps = data[0:,2]
        cdps = data[0:,3]
        pdmg = data[0:,4]
        cdmg = data[0:,5]
        x = np.arange(len(pdps))
    return x,pdps,cdps,pdmg,cdmg

################# HP/ARMOR DES BOSS #################

VG = [22021440,1910,"VG"]
GORSEVAL = [21628200,2597,"GORSEVAL"]
SABETHA = [34015256,2597,"SABETHA"]

SLOTHASOR = [18973828,2597,"SLOTHASOR"]
MATTHIAS = [25953840,2597,"MATTHIAS"]

KC = [55053600,1910,"KC"]
XERA_P1 = [11411538,2597,"XERA_P1"]
XERA_P2 = [12710140,2597,"XERA_P2"]

CAIRN = [19999998,2597,"CAIRN"]
MO = [22021440,2597,"MO"]
MOCM = [30000000,2597,"MO CM"]
SAMAROG = [29493000,2597,"SAMAROG"]
SAMAROGCM = [40000000,2597,"SAMAROG CM"]
DEIMOS_P1 = [29216168,2597,"DEIMOS 100-10%"]
DEIMOS_P2 = [4793274,2597,"DEIMOS 10-0%"]
DEIMOSCM_P1 = [35525963,2597,"DEIMOS CM 100-10%"]
DEIMOSCM_P2 = [4844604,2597,"DEIMOS CM 10-0%"]

SH = [35391600,2597,"SH"]
DHUUM = [32000000,2597,"SH CM"]
DHUUMCM = [40000000,2597,"DHUUM CM"]

################# LES SPÉ #################

pBsw = spe(*get_spe('pBsw'),np.array([225,217,40]),"pBsw",seuil=["up",80,1.25,"p"])
cScrg = spe(*get_spe('cScrg'),np.array([14,120,15]),"cScrg")
pCata = spe(*get_spe('pCata'),np.array([231,19,19]),"pCata",seuil=["down",50,1.2,"p"])