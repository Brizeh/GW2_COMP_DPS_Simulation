import numpy as np
import matplotlib.pyplot as plt
from specialization import*
from collections import Counter
from matplotlib.ticker import EngFormatter

def shortest_x(spe_list):      # Obtenir le temps le plus court de 'spe_list' pour reajuster la longueur des autres tableaux 
    x_min = len(spe_list[0].x)
    for spes in spe_list:
        if(len(spes.x)<x_min):
            x_min = len(spes.x)
    for spes in spe_list:
        spes.x, spes.pdps, spes.cdps, spes.pdmg, spes.cdmg = spes.x[:x_min], spes.pdps[:x_min], spes.cdps[:x_min], spes.pdmg[:x_min], spes.cdmg[:x_min]
    return

def sortSpe(spe_list):  # Fonction de copie des données des objets de spé
    spes = []
    for e in spe_list:
        perso = []
        perso.append(e.seuil)
        perso.append(e.pdps)
        perso.append(e.cdps)
        spes.append(perso)
    return spes 

def reajust_dmg(boss_HP,boss_armor,spe_list):
    spes = sortSpe(spe_list) # Copie des données des objets Spé
    Tdps = np.zeros(len(spe_list[0].x)) # Dps instantané de la compo totale
    seuils_up = [] # Compteur de seuils type UP (comme Bsw)
    seuils_down = [] # Compteur de seuils type DOWN (comme BTTH)

    for e in spes:  # Appliquer les degats de seuils_UP sur tout le fight

                    # Ici e = [[seuil="up"/"down", seuil_en_%, multiplicateur, "power" ou "condi"], np.array[pDPS], np.array[cDPS]]

        e[1]=e[1]*2597/boss_armor # Augmentation des dégats power sur armure 

        if(e[0][0]=="down"): 
            if(e[0][1] not in seuils_down): # Comptage des seuils_down UNIQUES
                seuils_down.append(e[0][1])
        if(e[0][0]=="up"):
            if(e[0][3]=="p"):
                e[1]=e[1]*e[0][2] # Si le bonus s'applique aux dégats power
            elif(e[0][3]=="c"):
                e[2]=e[2]*e[0][2] # Si le bonus s'applique aux dégats condi
            else:
                e[1]=e[1]*e[0][2]
                e[2]=e[2]*e[0][2] # Si le bonus s'applique aux dégats power et condi
            if(e[0][1] not in seuils_up): # Comptage des seuils_up UNIQUES
                seuils_up.append(e[0][1])
        Tdps=Tdps*1+e[1]+e[2]

    Tdmg = [0]  # Mettre à jour les degats pour re-évaluer les seuils_up
    for i in range(1,len(Tdps)):
        Tdmg.append(np.sum(Tdps[0:i]))
    Tdmg = np.array(Tdmg)

    if(len(seuils_up)!=0):
        for i in range(len(seuils_up)):    # Enlever les seuil_up par ordre décroissant
            dmgSeuil = boss_HP*(1-seuils_up[i]/100)
            idmgSeuil = np.where(Tdmg>=dmgSeuil)[0][0]
            Tdps = np.zeros(len(spe_list[0].x))
            for e in spes:
                if(e[0][1]==seuils_up[i]):
                    if(e[0][3]=="p"):
                        e[1][idmgSeuil:]=e[1][idmgSeuil:]/e[0][2] 
                    elif(e[0][3]=="c"):
                        e[2][idmgSeuil:]=e[2][idmgSeuil:]/e[0][2]
                    else:
                        e[1][idmgSeuil:]=e[1][idmgSeuil:]/e[0][2]
                        e[2][idmgSeuil:]=e[2][idmgSeuil:]/e[0][2]
                Tdps=Tdps*1+e[1]+e[2]          

    Tdmg = [0]  # Mettre à jour les degats pour évaluer les seuils_down
    for i in range(1,len(Tdps)):
        Tdmg.append(np.sum(Tdps[0:i]))
    Tdmg = np.array(Tdmg)

    if(len(seuils_down)!=0): # Ajouter les degats des seuil_down par ordre décroissant
        for i in range(len(seuils_down)):
            dmgSeuil = boss_HP*(1-seuils_down[i]/100)
            idmgSeuil = np.where(Tdmg>=dmgSeuil)[0][0]
            Tdps = np.zeros(len(spe_list[0].x))
            for e in spes:
                if(e[0][1]==seuils_down[i]):
                    if(e[0][3]=="p"):
                        e[1][idmgSeuil:]=e[1][idmgSeuil:]*e[0][2] # Si le bonus s'applique aux dégats power
                    elif(e[0][3]=="c"):
                        e[2][idmgSeuil:]=e[2][idmgSeuil:]*e[0][2] # Si le bonus s'applique aux dégats condi
                    else:
                        e[1][idmgSeuil:]=e[1][idmgSeuil:]*e[0][2]
                        e[2][idmgSeuil:]=e[2][idmgSeuil:]*e[0][2] # Si le bonus s'applique aux dégats power et condi
                Tdps=Tdps*1+e[1]+e[2]

    Tdmg = [0]  # Mettre à jour les degats pour le rendu des dégats final
    for i in range(1,len(Tdps)):
        Tdmg.append(np.sum(Tdps[0:i]))
    Tdmg = np.array(Tdmg)

    iKill = np.where(Tdmg>=boss_HP)[0][0]  # Reduire le graph au moment ou ya kill du BOSS
    Tdmg = Tdmg[:iKill+1]
    xTdmg = np.arange(len(Tdmg))

    return xTdmg,Tdmg

def get_color_comp(spe_list): # Get la couleur de la comp (ex: Bsw+Cata = Jaune+Rouge => Orange)
    c = np.zeros(3)
    for e in spe_list:
        c = c + e.color
    c = c/len(spe_list)/255
    return c

def get_name_comp(spe_list): # Get les noms de spé à afficher dans la compo pour le graph
    names = []
    for e in spe_list:
        names.append(e.name)
    names = Counter(names)
    s = ""
    for e in names:
        s = s + str(names[e]) + " " + e + " | "
    s = "["+s[0:len(s)-3]+"]"
    return s

def graph_comp(boss,spe_list,modeDPS="dpsFinal"): # Grapher un boss avec une compo

    shortest_x(spe_list)
    x,y = reajust_dmg(*boss[:-1],spe_list)
    x[0]=1 #sécurité pour la division par 0
    if(modeDPS=="dpsFinal"):  # choix du mode d'affichage degats cummulés ou dps 
        y = y/x
        plt.ylabel("Dmg/s")

    n = get_name_comp(spe_list)
    c = get_color_comp(spe_list) # A utiliser si on veut utiliser les couleurs de classes de Arcdps #Rip les daltoniens

    if(DALTONIEN_MODE):
        ax.plot(y,marker='o',markersize=3,label=n) 
    else:
        ax.plot(y,marker='o',markersize=3,label=n,color=c)
    graphs.append(y)
    return

def get_title_boss(boss): # Get le titre du graph = NOM_DU_BOSS + HP_BOSS 
    s = boss[2] + " = " + str(boss[0])+"HP"
    plt.title(s)

fig, ax = plt.subplots()

graphs = []

#####################################################################################################################
###################################### PARTIE SET UP DE COMPO #######################################################
#####################################################################################################################




DALTONIEN_MODE = 0  # 0 pour les couleurs de classes / 1 pour couleur mode daltonien (cc Ravi)

'''

Les spé actuellement disponibles pour des tests : 

    DPS : [pCata, cScrg, pBsw, pSlb, pHolo, cHarb, pWeav, pSpb,
           pDar, pTemp, cReap, cDar, cRen]

    ALAC : [cARen]
    
    QUICK : [cQFb, cQUnt]

'''

dpsStyle = "dpsFinal"   # Ya "cummulative" et "dpsFinal"
Boss = CAIRN # Le boss ici

Compo = [pBsw]*6+[cARen]*2+[cQUnt]*2    # La Compo ici 6 Bsw et 4 cARen COPIUMMMMMMMMMMMMMMMMM
graph_comp(Boss,Compo,modeDPS=dpsStyle) 

Compo = [pWeav]*6+[cARen]*2+[cQUnt]*2      # La Compo ici 10 Scrg oui
graph_comp(Boss,Compo,modeDPS=dpsStyle)

Compo = [pSlb]*6+[cARen]*2+[cQUnt]*2      # La Compo ici 10 Scrg oui
graph_comp(Boss,Compo,modeDPS=dpsStyle)

Compo = [pHolo]*6+[cARen]*2+[cQUnt]*2      # La Compo ici 10 Scrg oui
graph_comp(Boss,Compo,modeDPS=dpsStyle)




#####################################################################################################################
###################################### PARTIE SET UP DE COMPO #######################################################
#####################################################################################################################

# Paramètres pour pauffiner le graphique

yMax=0 # Ajuster la fenetre
xMax=0
for i in range(len(graphs)):
    tempy = np.amax(graphs[i][1:])
    tempx = len(graphs[i])
    if(tempx>=xMax):
        xMax = tempx
    if(tempy>=yMax):
        yMax = tempy

ysup = yMax*1.04
yinf = -0.04*yMax
xsup = xMax*1.02
xinf = -xMax*0.02

arrondi1 = 10**3 # Ajuster les échelles
arrondi2 = 10**5
if(dpsStyle=="dpsFinal"):
    yStep = int(np.round((ysup/25)/arrondi1)*arrondi1)
else:
    yStep = int(np.round((ysup/25)/arrondi2)*arrondi2)
ax.set_xticks(np.arange(0, 1000, step=2)) 
ax.set_yticks(np.arange(0,ysup,yStep))
ax.set_xlim([xinf,xsup])
ax.set_ylim([yinf,ysup])

get_title_boss(Boss) # Le titre

xtemp = np.linspace(0,600,2000) # Afficher la barre de mort du BOSS
if(dpsStyle=="dpsFinal"):
    ax.plot(xtemp[1:],Boss[0]/xtemp[1:],color="black",label="Mort du Boss",linestyle='--')
elif(dpsStyle=="cummulative"):
    ax.plot(xtemp,np.ones(len(xtemp))*Boss[0],color="black",label="Mort du Boss",linestyle='--')

if(DALTONIEN_MODE): # Salut les daltoniens
    plt.style.use('tableau-colorblind10')

formatter0 = EngFormatter() # Reformatage des textes puis affichage final
ax.yaxis.set_major_formatter(formatter0)
ax.set_xlabel("Time (s)")
ax.grid()
ax.legend(loc='best')
plt.show()