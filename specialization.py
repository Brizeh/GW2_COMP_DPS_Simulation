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
        data = np.array(data[2:]).astype(np.float64)
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

Q1 = [19268760,2293,"Q1"]
Q1CM = [21195636,2293,"Q1 CM"]

ADINA = [22611300,2597,"ADINA"]
ADINACM = [24872430,2597,"ADINA CM"]

################# LES SPÉ #################

cWar = np.array([225,217,40])
cNecro = np.array([14,120,15])
cElem = np.array([231,19,19])
cRev = np.array([144,12,63])
cGuard = np.array([38,229,226])
cEngi = np.array([161,111,52])
cRanger = np.array([164,216,53])
cMesmer = np.array([205,49,229])
cThief = np.array([185,122,207])

##################### pDPS #####################

pBsw = spe(*get_spe('pBsw'),cWar,"pBsw",seuil=["up",80,1.25,"p"])
pSlb = spe(*get_spe('pSlb'),cRanger,"pSlb")
pHolo = spe(*get_spe('pHolo'),cEngi,"pHolo")
pCata = spe(*get_spe('pCata'),cElem,"pCata",seuil=["down",50,1.2,"p"])
pWea = spe(*get_spe('pWea'),cElem,"pWea",seuil=["down",50,1.2,"p"])
pSpb = spe(*get_spe('pSpb'),cWar,"pSpb")
pDar = spe(*get_spe('pDar'),cThief,"pDar")
pTmp = spe(*get_spe('pTmp'),cElem,"pTmp")
pBer = spe(*get_spe('pBer'),cWar,"pBer")
pHar = spe(*get_spe('pHar'),cNecro,"pHar")
pVin = spe(*get_spe('pVin'),cRev,"pVin",seuil=["up",80,1.2,"p"])
pDed = spe(*get_spe('pDed'),cThief,"pDed")

##################### cDPS #####################

cScg = spe(*get_spe('cScg'),cNecro,"cScg")
cHar = spe(*get_spe('cHar'),cNecro,"cHar")
cRea = spe(*get_spe('cRea'),cNecro,"cRea")
cDar = spe(*get_spe('cDar'),cThief,"cDar")
cRen = spe(*get_spe('cRen'),cRev,"cRen")
cVir = spe(*get_spe('cVir'),cMesmer,"cVir")
cMec = spe(*get_spe('cMec'),cEngi,"cMec")
cWil = spe(*get_spe('cWil'),cGuard,"cWil")
cDru = spe(*get_spe('cDru'),cRanger,"cDru")

##################### pALAC #####################

paBsw = spe(*get_spe('paBsw'),cWar,"paBsw",seuil=["up",80,1.25,"p"])
paTmp = spe(*get_spe('paTmp'),cElem,"paTmp")
paMec = spe(*get_spe('paMec'),cEngi,"paMec")
paChr = spe(*get_spe('paChr'),cMesmer,"paChr")

##################### cALAC #####################

caRen = spe(*get_spe('caRen'),cRev,"caRen")
caRen_NA = spe(*get_spe('caRen_NA'),cRev,"caRen_NA")
caScg = spe(*get_spe('caScg'),cNecro,"caScg")
caMir = spe(*get_spe('caMir'),cMesmer,"caMir")
caTmp = spe(*get_spe('caTmp'),cElem,"caTmp")

##################### pQUICK #####################

pqHer = spe(*get_spe('pqHer'),cRev,"pqHer")
pqChr = spe(*get_spe('pqChr'),cMesmer,"pqChr")
pqScr = spe(*get_spe('pqScr'),cEngi,"pqScr")

##################### cQUICK #####################

cqFb = spe(*get_spe('cqFb'),cGuard,"cqFb")
cqUnt = spe(*get_spe('cqUnt'),cRanger,"cqUnt")
cqHar = spe(*get_spe('cqHar'),cNecro,"cqHar")
cqBer = spe(*get_spe('cqBer'),cWar,"cqBer")










