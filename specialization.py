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

pBsw = spe(*get_spe('pBsw'),cWar,"pBsw",seuil=["up",80,1.25,"p"])
cScrg = spe(*get_spe('cScrg'),cNecro,"cScrg")
pCata = spe(*get_spe('pCata'),cElem,"pCata",seuil=["down",50,1.2,"p"])
cARen = spe(*get_spe('cARen'),cRev,"cARen")
cARen_NA = spe(*get_spe('cARen_NA'),cRev,"cARen_NA")
cQFb = spe(*get_spe('cQFb'),cGuard,"cQFb")
pSlb = spe(*get_spe('pSlb'),cRanger,"pSlb")
pHolo = spe(*get_spe('pHolo'),cEngi,"pHolo")
cQUnt = spe(*get_spe('cQUnt'),cRanger,"cQUnt")
cHarb = spe(*get_spe('cHarb'),cNecro,"cHarb")
pWeav = spe(*get_spe('pWeav'),cElem,"pWeav",seuil=["down",50,1.2,"p"])
pSpb = spe(*get_spe('pSpb'),cWar,"pSpb")
pDar = spe(*get_spe('pDar'),cThief,"pDar")
pTemp = spe(*get_spe('pTemp'),cElem,"pTemp")
cReap = spe(*get_spe('cReap'),cNecro,"cReap")
cDar = spe(*get_spe('cDar'),cThief,"cDar")
cRen = spe(*get_spe('cRen'),cRev,"cRen")
pBers = spe(*get_spe('pBers'),cWar,"pBers")
cVirt = spe(*get_spe('cVirt'),cMesmer,"cVirt")