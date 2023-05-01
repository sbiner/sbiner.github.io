# ajout de htmlgen et de biner
rep_htmlgen='../../../../../../Local/modules_externes/HTMLgen'
rep_htmlgen="/Users/sbiner/cloud/Sync/local/modules_externes/HTMLgen"
rep_biner='../../../../../CODE/python/stable'
rep_biner="/Users/sbiner/cloud/Sync/perso/CODE/python/stable"
import sys
sys.path.append(rep_htmlgen)
sys.path.append(rep_biner)

from HTMLgen import *
import HTMLcolors as HTMLcolors
import time, biner
import string
#import pandas as pd

# lecture du fichier csv
fh = open("ze_pool_2023 - Feuille 1.csv")
lines = fh.read().splitlines()
fh.close()

clefs_r1 = lines[0].upper().split(",")[:-1]
clefs_r1[0] = "nom"

r1 = []
for ll in lines[1:]:
    tampon = ll.split(",")
    tampon2 = tampon[:1] + [cc.upper() for cc in tampon[1:]]
    r1.append(tampon2)
    print(r1)





# 1/0          
# clefs_r1='nom  CAR/BOS TOR/TB NYR/PIT FLO/WAS MIN/STL EDM/LA COL/NAS CAL/DAL'.split()
# r1=[]
# r1.append('Fred, BOS 4, TB 4, PIT 4, WAS 4, STL 4, LA 4, NAS 4, DAL 4, NAS'.split(','))
# r1.append('Travis, BOS 6, TOR 7, NYR 6, FLO 5, MIN 7, LA 5, COL 4, CAL 5, CAL'.split(','))
# r1.append('Alain, CAR 7, TB 7, NYR 6, FLO 6, MIN 7, EDM 7, COL 4, CAL 5, CAL'.split(','))
# r1.append('Pat, CAR 5, TB 6, PIT 7, FLO 6, MIN 7, EDM 5, COL 5, CAL 5, COL  '.split(','))
# r1.append('Do, BOS 6, TB 6, MYR 7, WAS 7, MIN 6, LA 7, COL 6, DAL 6, CAR'.split(','))
# r1.append('Mike, CAR 7, TB 6, NYR 5, FLO 7, MIN 6, EDM 7, COL 4, CAL 4, COL'.split(','))
# r1.append('Valerie, CAR 6, TB 7, PIT 7, FLO 5, MIN 7, EDM 6, COL 5, DAL 6, COL'.split(','))
# r1.append('Phil R., CAR 6, TB 7, NYR 6, FLO 5, MIN 6, EDM 5, COL 4, CAL 5, COL'.split(','))
# r1.append('Phil P., CAR 6, TB 7, NYR 6, FLO 7, STL 6, LA 6, COL 6, CAL 7, COL'.split(','))
# r1.append('Seb, CAR 6, TB 6, NYR 6, FLO 6, MIN 7, EDM 6, COL 5, CAL 6, COL'.split(','))
# r1.append('Norm, BOS 6, TB 5, PIT 6, FLO 7, STL 7, EDM 7, COL 4, CAL 6, TB'.split(','))
# r1.append('Daniel, BOS 6, TB 6, NYR 6, FLO 6, STL 6, EDM 7, COL 5, CAL 5, COL'.split(','))
# r1.append('Chee, BOS 6, TB 6, NYR 7, FLO 5, MIN 6, EDM 5, COL 7, CAL 4, TB'.split(','))
# r1.append('Yorann, BOS 5, TB 5, PIT 5, WAS 5, MIN 7, EDM 6, NAS 6, DAL 7, TB'.split(','))
# r1.append('Etienne, CAR 6, TB 7, NYR 6, FLO 6, MIN 6, EDM 6, COL 5, CAL 6, CAR'.split(','))


# On separe la liste de coup de circuit des autres
listeCs=[]
listeR1=[]
for r in r1 :
    listeCs.append([r[0],r[-1]])
    listeR1.append(r[0:-1])
r1=listeR1


clefs_r2='nom '.split()
r2=[]


clefs_r3='nom '.split()
r3=[]


clefs_r4='nom '.split()
r4=[]


res_r1={"DAL/MIN":"DAL 6", "TOR/TB": "TOR 6", "EDM/LAK":"EDM 6", "VGK/WIN":"VGK 5", "CAR/NYI":"CAR 6"}        
res_r2={}
res_r3={}
res_r4={}
res=[res_r1,res_r2,res_r3,res_r4]
pts_gagnant=[10,15,20,25]
pts_matchs=[2,3,4,5]
pts_coup_circuit=40

# on enleve la colonne contenant le nom pour les rondes autres que 1

clefs=clefs_r1+clefs_r2[1:]+clefs_r3[1:]+clefs_r4[1:]
r2_modif=[]
for n in r2 :
    r2_modif.append(n[1:])
r3_modif=[]
for n in r3:
    r3_modif.append(n[1:])
r4_modif=[]
for n in r4:
    r4_modif.append(n[1:])

# on batit le tableau avec les choix de toutes les rondes
ronde=[]
for j in range(len(r1)) :
#   choix=r1[j]+r2_modif[j]+r3_modif[j]+r4_modif[j]
    choix=r1[j]
    if len(r2_modif) : choix=choix+r2_modif[j]
    if len(r3_modif) : choix=choix+r3_modif[j]
    if len(r4_modif) : choix=choix+r4_modif[j]

    ronde.append(choix)

# On bati le dict des choix de tout le monde
choix=[]
for j in range(len(ronde)) :
    ###choix.append(dict(zip(clefs_r1,r1[j])))
    choix.append(dict(list(zip(clefs,ronde[j]))))

##################################################
# on ecrit un petit tableau des choix   

l=''
for c in clefs_r1 : l=l+"%10s" % c
print(l)

for j in range(len(r1)) :
    l=''
    for c in clefs_r1 :
        cc=choix[j][c]
        l=l+"%10s" % cc
    print(l)

# classement en ordre alphabetique des noms
choix = biner.classe_liste_dict(choix,'nom',1)
listeCs.sort(key = lambda x: x[0])


##################################################
# calcul des points

classement=[]
clefs_classement=['nom','ronde 1','ronde 2','demie-finale','finale','CIRCUIT','total']

# on boucle sur les participants
for i,p in enumerate(choix) :
    pts=[0,0,0,0,0]
    print('*'*70)
    print(p['nom'])
    print('*'*70)
    # boucle sur les choix
    for c in list(p.keys()) :
        if c != 'nom' :
            # trouver la ronde du choix
            ronde=0
            if c in res_r1 : ronde=1
            elif c in res_r2 : ronde=2
            elif c in res_r3 : ronde=3
            elif c in res_r4 : ronde=4

            print('serie :',c, ', ronde :', ronde)

            #else :
            #print 'serie ',c,' pas finie'
            if ronde != 0 :
                cc=p[c]
                print('cc=',cc)
                choix_g,choix_m=string.split(cc)
                choix_g=string.strip(choix_g)
                choix_m=int(choix_m)
                resultat=res[ronde-1][c]
                res_g,res_m=string.split(resultat)
                res_g=string.strip(res_g)
                res_m=int(res_m)
                print('nom=',p['nom'])
                print('choix=',choix_g,choix_m)
                print('res=',res_g,res_m)
                if choix_g == res_g :
                    print('bon g')
                    pts[ronde-1]=pts[ronde-1]+pts_gagnant[ronde-1]
    #                   if choix_m == res_m :
    #                       print 'bon m'
    #                       pts[ronde-1]=pts[ronde-1]+pts_matchs[ronde-1]
                if choix_m == res_m :
                    print('bon m')
                    pts[ronde-1]=pts[ronde-1]+pts_matchs[ronde-1]
                # traitement du coup de circuit
                #if ronde == 4 :
                #   if listeCs[i][-1]==res_g:
                #       pts[ronde]=pts_coup_circuit
                if listeCs[i][-1].strip() == res_g :
                    print('ronde =', ronde)
                    pts[4] = max(10*ronde, pts[4])
                    print("*** pts pour Coup de circuit ***", ronde, pts[4])
                    

    # fin boucle sur les choix
    # on ajoute la ligne au classement
    val=[p['nom'],pts[0],pts[1],pts[2],pts[3],pts[4],sum(pts)]
    print(val)
    classement.append(dict(list(zip(clefs_classement,val))))
# fin boucle sur les participants

# classement du classement par le total
classement=biner.classe_liste_dict(classement,'total',-1)

print(classement)


##################################################
# on genere la page web des choix

page_choix=SimpleDocument('zp2023rc.html')


# on prepare le lien vers l'entete
page_choix.append(Name('entete'))
lien_entete=Href('#entete',Font('retour en haut',size='-1'))

# affichage de la derniere mise a jour
#texte_widget=RawText('<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,29,0" width="158" height="140"><param name="movie"value="nameofwidget.swf"><param name="wmode" value="transparent"><param name=quality value=high><embed src="canadienspresentaway.swf" quality=high pluginspage="http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash" type="application/x-shockwave-flash" width="158" height="140" wmode="transparent"></embed></object>')
font_maj=Font(size='0')
texte_maj='derniere mise a jour:'+time.strftime('%d/%m/%Y',time.localtime())
#texte_maj=Text('derniere mise a jour:')
#texte_maj.append(texte_widget)
#texte_maj.append(time.strftime('/%m/%Y',time.localtime()))

font_maj.append(texte_maj)
page_choix.append(Paragraph(font_maj,align='right'))




texte=Text()
coupe=Image('images/stanleycup.jpg',width=50)
texte.append(coupe)
texte.append(Font('Ze Pool 2023',color=HTMLcolors.RED,size='+2'))
texte.append(coupe)
page_choix.append(Heading(1,texte,align='center'))

texte=Text()
texte.append("Bienvenue sur la page officielle du pool des series de la coupe Stanley")
page_choix.append(Heading(2,texte,align='center'))
texte=Text()
#pdaj=Image('images/photo_bob1.jpg',width=500,align='center')
#pdaj=Image('images/flight132-2-1.psd.jpg',width=500,align='center')
#pdaj=Image('images/Jolly_jumper_copie.jpg',width=500,align='center')
#pdaj=Image('images/bagues.png',width=200,align='center')
pdaj=Image('images/go_habs_go.jpg',width=200,align='center')

texte.append(BR())
texte.append(pdaj)
texte.append('photo piquee de sportnographe.com')
texte.append(BR())
#texte.append("Cette annee encore, ce site est dedie a Bob Gainey. Premier a le planter, je me dois de reconnaitre qu'il semble que cette annee son immobilisme etait la chose a faire ... ou a ne pas faire en fait. En tout cas, il demeure qu'il s'est bien abstenu de faire ce qu'il ne fallait pas faire, encore que c'est peut-etre pas faute d'avoir voulu le faire. D'ailleurs Bob m'inspire de son immobilisme et je ne changerai rien a mon site web qui ressemble etrangement a tous les anciens que j'ai fait. Pourquoi changer une formule gagnante? Bon treve de billevesee, place a l'action:")
#texte.append(P())
page_choix.append(texte)

liste=List()
liste.append("Comme d'habitude, un * a cote de votre nom indique que vous avez paye votre 5$. Bonnes series.")
page_choix.append(liste)

texte=Text("Place a l'action:")
page_choix.append(texte)

#page_choix.append(texte)
page_choix.append(HR())

# on prepare la liste de liens
liste_liens=List()

##################################################
# page des resultats
page_res=SimpleDocument('zp2023rc.html')
#ligne horizontale
page_res.append(HR())
#ancre de cette part et ajout du lien
page_res.append(Name('resultats'))
liste_liens.append(Href('#resultats','resultats des series'))
#ajout du lien vers l'entete
page_res.append(lien_entete)
# debut de la page
page_res.append(Heading(2,'resultats des series'))

tres=TableLite()

ronde=0
# boucle sur les ronde
for r in res :
    ronde=ronde+1
    # s'il y a de resultats pour la ronde on fait un tableau
    if len(r) > 0 :
        t_ronde=TableLite(bgcolor=HTMLcolors.GRAY3,border=1)
        l=TR()
        nom_ronde={1:'ronde1',2:'ronde2',3:'demie-finale',4:'finale'}[ronde]
        t_ronde.append(TR(TD(Font(nom_ronde,color=HTMLcolors.RED5),colspan=2,align='center',width='100%')))
        l.append(TH(Font('serie',color=HTMLcolors.RED5)))
        l.append(TH(Font('gagnant',color=HTMLcolors.RED5)))
        t_ronde.append(l)
        for s in list(r.keys()) :
            l=TR()
            cellule=TD(Font(Strong(s),color=HTMLcolors.BLACK))
            l.append(cellule)
            cellule=TD(Font(r[s],color=HTMLcolors.BLACK))
            l.append(cellule)
            t_ronde.append(l)
        tres.append(TH(t_ronde,valign='top'))

page_res.append(tres)
    

##################################################
# page du classement
page_classement=SimpleDocument('zp2023rc.html')
#ligne horizontale
page_classement.append(HR())
# ancre de cette partie et ajout du lien
page_classement.append(Name('classement'))
liste_liens.append(Href('#classement','classement'))
# ajout du lien vers l'entete
page_classement.append(lien_entete)
# debut de la page
page_classement.append(Heading(2,'classement'))
# ajout du tableau
ligne=TR()
# ajout des
t=TableLite(bgcolor=HTMLcolors.GRAY3,border=1)
#entete
for c in clefs_classement :
    texte="%20s" % c
    ligne.append(TH(Font(texte,color=HTMLcolors.RED5)))
t.append(ligne)
# nom des participant et resultats
for i in range(len(classement)) :
    ligne=TR()
    for c in clefs_classement :
        cc=classement[i][c]
        texte="%20s" % cc
        couleur=HTMLcolors.BLACK
        if c == 'nom' : couleur=HTMLcolors.RED5
        ligne.append(TD(Font(texte,color=couleur)))
    t.append(ligne)
# ajout du tableau a la page
page_classement.append(t)

##################################################
# page des choix 

page_r1=SimpleDocument('zp2023rc.html')
#ligne horizontale
page_r1.append(HR())
# ancre de cette partie et ajout du lien
page_r1.append(Name('choix'))
liste_liens.append(Href('#choix','choix pour chaque ronde'))
# ajout du lien vers l'entete
page_r1.append(lien_entete)
# debut de la page

# choix ronde 1
page_r1.append(Heading(2,'choix pour la premiere ronde'))
# ajout du tableau
t=TableLite(bgcolor=HTMLcolors.GRAY3,border=1)
ligne=TR()
#entete
for c in clefs_r1 :
    texte="%15s" % c
    ligne.append(TH(Font(texte,color=HTMLcolors.RED5)))
# choix coup de circuit
texte="%15s" % 'coup de circuit'
ligne.append(TH(Font(texte,color=HTMLcolors.RED5)))
t.append(ligne)

#noms des participants et choix
for j in range(len(r1)) :
    ligne=TR()
    for c in clefs_r1 :
        cc=choix[j][c]
        texte="%15s" % cc
        couleur=HTMLcolors.BLACK
        if c == 'nom' : couleur=HTMLcolors.RED5
        ligne.append(TD(Font(texte,color=couleur)))
    # choix coup de circuit
    texte="%15s" % listeCs[j][-1]
    ligne.append(TD(Font(texte,color=couleur)))
    t.append(ligne)

# on ajoute le tableau a la page 
page_r1.append(t)

# choix ronde 2
page_r1.append(Heading(2,'choix pour la deuxieme ronde'))
# ajout du tableau
t=TableLite(bgcolor=HTMLcolors.GRAY3,border=1)
ligne=TR()
# entete
for c in clefs_r2 :
    texte="%15s" % c
    ligne.append(TH(Font(texte,color=HTMLcolors.RED5)))
t.append(ligne)
#noms des participants et choix
for j in range(len(r2)) :
    ligne=TR()
    for c in clefs_r2 :
        cc=choix[j][c]
        texte="%15s" % cc
        couleur=HTMLcolors.BLACK
        if c == 'nom' : couleur=HTMLcolors.RED5
        ligne.append(TD(Font(texte,color=couleur)))
    t.append(ligne)

# on ajoute le tableau a la page 
page_r1.append(t)

# choix ronde 3
page_r1.append(Heading(2,'choix pour les demie-finales'))
# ajout du tableau
t=TableLite(bgcolor=HTMLcolors.GRAY3,border=1)
ligne=TR()
# entete
for c in clefs_r3 :
    texte="%15s" % c
    ligne.append(TH(Font(texte,color=HTMLcolors.RED5)))
t.append(ligne)
#noms des participants et choix
for j in range(len(r3)) :
    ligne=TR()
    for c in clefs_r3 :
        cc=choix[j][c]
        texte="%15s" % cc
        couleur=HTMLcolors.BLACK
        if c == 'nom' : couleur=HTMLcolors.RED5
        ligne.append(TD(Font(texte,color=couleur)))
    t.append(ligne)
# on ajoute le tableau a la page 
page_r1.append(t)

# choix ronde 4
page_r1.append(Heading(2,'choix pour la finale'))
# ajout du tableau
t=TableLite(bgcolor=HTMLcolors.GRAY3,border=1)
ligne=TR()
#entete
for c in clefs_r4 :
    texte="%15s" % c
    ligne.append(TH(Font(texte,color=HTMLcolors.RED5)))
t.append(ligne)
#noms des participants et choix
for j in range(len(r4)) :
    ligne=TR()
    for c in clefs_r4 :
        cc=choix[j][c]
        texte="%15s" % cc
        couleur=HTMLcolors.BLACK
        if c == 'nom' : couleur=HTMLcolors.RED5
        ligne.append(TD(Font(texte,color=couleur)))
    t.append(ligne)
# on ajoute le tableau a la page 
page_r1.append(t)
    


##################################################
# reglements
page_regle=SimpleDocument('zp2023rc.html')
#ligne horizontale
page_regle.append(HR())
# ancre de cette partie et ajout du lien
page_regle.append(Name('regle'))
liste_liens.append(Href('#regle','reglements'))
# ajout du lien vers l'entete
page_regle.append(lien_entete)
# debut de la page

# choix ronde 1
page_regle.append(Heading(2,'reglements'))

liste=OrderedList()
liste.append('le premier recoit tout ce qui reste apres les prix des 2e et 3e.')
liste.append('le deuxieme recoit 2 fois sa mise.')
liste.append('le troisieme recupere sa mise.')
liste.append('la mise est de 5$ cette annee.')

page_regle.append(liste)

messg="""
Les points sont les suivants pour les gagnant de chaque serie 
et pour le nombre de match (peu importe le gagnant) en fonction de la ronde
"""
page_regle.append(Text(messg))

t=TableLite(bgcolor=HTMLcolors.GRAY3,border=1)
l=TR()
l.append(TH(Font('ronde',color=HTMLcolors.RED5)))
l.append(TH(Font('gagnant de la serie',color=HTMLcolors.RED5)))
l.append(TH(Font('nombre de matchs',color=HTMLcolors.RED5)))
t.append(l)
l=TR()
l.append(TH(Font('ronde 1',color=HTMLcolors.RED5)))
l.append(TD(Font('10',align='right',color=HTMLcolors.BLACK)))
l.append(TD(Font('2',align='right',color=HTMLcolors.BLACK)))
t.append(l)
l=TR()
l.append(TH(Font('ronde 2',color=HTMLcolors.RED5)))
l.append(TD(Font('15',align='right',color=HTMLcolors.BLACK)))
l.append(TD(Font('3',align='right',color=HTMLcolors.BLACK)))
t.append(l)
l=TR()
l.append(TH(Font('demie-finale',color=HTMLcolors.RED5)))
l.append(TD(Font('20',align='right',color=HTMLcolors.BLACK)))
l.append(TD(Font('4',align='right',color=HTMLcolors.BLACK)))
t.append(l)
l=TR()
l.append(TH(Font('finale',color=HTMLcolors.RED5)))
l.append(TD(Font('25',align='right',color=HTMLcolors.BLACK)))
l.append(TD(Font('5',align='right',color=HTMLcolors.BLACK)))
t.append(l)
l=TR()
l.append(TH(Font('choix coup de circuit',color=HTMLcolors.RED5)))
l.append(TD(Font('10 points par ronde',align='right',color=HTMLcolors.BLACK)))
#l.append(TD(Font('5',align='right',color=HTMLcolors.BLACK)))
t.append(l)

page_regle.append(t)

# inclusion de la musique

#<embed SRC=hockey.wav AUTOPLAY=true AUTOSTART=true HIDDEN=true LOOP=false height="50"
#width="200" >
musique=Embed(src='wav/hockey.wav',autoplay='true',autostart='true',hidden='true',loop='false',height=50,width=50)
musique1=Embed(src='wav/canadiens_gagne_coupe_24.mp3',autoplay='true',autostart='true',hidden='true',loop='false',height=50,width=50)

#ecriture de la page

page_choix.append(musique)
page_choix.append(musique1)
page_choix.append(liste_liens)
page_choix.append(page_res)
page_choix.append(page_classement)
page_choix.append(page_r1)
page_choix.append(page_regle)
page_choix.write('index.html')

                  
