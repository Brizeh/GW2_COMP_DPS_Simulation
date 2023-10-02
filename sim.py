import numpy as np
import matplotlib.pyplot as plt
from specialization import*
from collections import Counter

def shortest_x(spe_list):      #Obtenir le temps le plus court de 'spe_list' pour reajuster la longueur des autres tableaux 
    x_min = len(spe_list[0].x)
    for spes in spe_list:
        if(len(spes.x)<x_min):
            x_min = len(spes.x)
    for spes in spe_list:
        spes.x, spes.pdps, spes.cdps, spes.pdmg, spes.cdmg = spes.x[:x_min], spes.pdps[:x_min], spes.cdps[:x_min], spes.pdmg[:x_min], spes.cdmg[:x_min]
    return

def sortSpe(spe_list):  # Fonction copie des données des objets
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
    Tdps = np.zeros(len(spe_list[0].x)) # Dps instantané total
    seuils_up = [] # Compteur de seuils type UP (comme Bsw)
    seuils_down = [] # Compteur de seuils type DOWN

    for e in spes:  # Appliquer les degats de seuils sur tout le fight
        e[1]=e[1]*2597/boss_armor #Augmentation des dégats power sur armure 

        if(e[0][0]=="down"):
            if(e[0][1] not in seuils_down):
                seuils_down.append(e[0][1])
        if(e[0][0]=="up"):
            if(e[0][3]=="p"):
                e[1]=e[1]*e[0][2]
            elif(e[0][3]=="c"):
                e[2]=e[2]*e[0][2]
            else:
                e[1]=e[1]*e[0][2]
                e[2]=e[2]*e[0][2]
            if(e[0][1] not in seuils_up):
                seuils_up.append(e[0][1])
        Tdps=Tdps*1+e[1]+e[2]

    Tdmg = [0]  # Mettre à jour les degats pour évaluer les seuils up
    for i in range(1,len(Tdps)):
        Tdmg.append(np.sum(Tdps[0:i]))
    Tdmg = np.array(Tdmg)

    if(len(seuils_up)!=0):
        for i in range(len(seuils_up)):    #Enlever les seuil up par ordre décroissant
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

    Tdmg = [0]  # Mettre à jour les degats pour évaluer les seuils down (comme BTTH)
    for i in range(1,len(Tdps)):
        Tdmg.append(np.sum(Tdps[0:i]))
    Tdmg = np.array(Tdmg)

    if(len(seuils_down)!=0): # Ajouter les degats des seuil down par ordre décroissant
        for i in range(len(seuils_down)):
            dmgSeuil = boss_HP*(1-seuils_down[i]/100)
            idmgSeuil = np.where(Tdmg>=dmgSeuil)[0][0]
            Tdps = np.zeros(len(spe_list[0].x))
            for e in spes:
                if(e[0][1]==seuils_down[i]):
                    if(e[0][3]=="p"):
                        e[1][idmgSeuil:]=e[1][idmgSeuil:]*e[0][2]
                    elif(e[0][3]=="c"):
                        e[2][idmgSeuil:]=e[2][idmgSeuil:]*e[0][2]
                    else:
                        e[1][idmgSeuil:]=e[1][idmgSeuil:]*e[0][2]
                        e[2][idmgSeuil:]=e[2][idmgSeuil:]*e[0][2]
                Tdps=Tdps*1+e[1]+e[2]

    Tdmg = [0]  # Mettre à jour les degats pour le rendu des dégats final
    for i in range(1,len(Tdps)):
        Tdmg.append(np.sum(Tdps[0:i]))
    Tdmg = np.array(Tdmg)

    iKill = np.where(Tdmg>=boss_HP)[0][0]  # Reduire le graph au moment ou ya kill du BOSS
    Tdmg = Tdmg[:iKill+1]
    xTdmg = np.arange(len(Tdmg))

    return xTdmg,Tdmg

def get_color_comp(spe_list): # Get la couleur de comp
    c = np.zeros(3)
    for e in spe_list:
        c = c + e.color
    c = c/len(spe_list)/255
    return c

def get_name_comp(spe_list): # Get les noms de spé
    names = []
    for e in spe_list:
        names.append(e.name)
    names = Counter(names)
    s = ""
    for e in names:
        s = s + str(names[e]) + " " + e + " | "
    s = s[0:len(s)-2]
    return s

def graph_comp(boss,spe_list,modeDPS="dpsFinal"): # Grapher un boss avec une compo
    shortest_x(spe_list)
    x,y = reajust_dmg(*boss[:-1],spe_list)
    if(modeDPS=="dpsFinal"):
        y = y/x
        plt.ylabel("Dmg/s")
    n = get_name_comp(spe_list)
    c = get_color_comp(spe_list)
    plt.plot(y,marker='o',markersize=3,label=n)
    ysup = np.amax(y[1:])*1.04
    yinf = -0.04*np.amax(y[1:])
    xsup = np.amax(x)*1.02
    xinf = -np.amax(x)*0.02
    plt.xlim([xinf,xsup])
    plt.ylim([yinf,ysup])
    return

def get_title_boss(boss): # Get le titre du graph
    s = boss[2] + " = " + str(boss[0])+"HP"
    plt.title(s)





Boss = CAIRN

for i in range(6): # Test de plusieurs compo mélange cata et bsw
    graph_comp(Boss,[pCata]*(10-i*2)+[pBsw]*i*2,modeDPS="dpsFinal")





spe_list = [pBsw,cScrg,pCata]  # Param pour pauffiner le graphique
get_title_boss(Boss)
xtemp = np.arange(len(spe_list[0].x))
plt.plot(xtemp,Boss[0]/xtemp,color="black",label="Mort du Boss",linestyle='--')
#plt.plot(xtemp,np.ones(len(xtemp))*Boss[0],color="black")
plt.style.use('tableau-colorblind10')
plt.ticklabel_format(style='plain')
plt.xlabel("Time (s)")
plt.grid()
plt.legend(loc='best')
plt.show()