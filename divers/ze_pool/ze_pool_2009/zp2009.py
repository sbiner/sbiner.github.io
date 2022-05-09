
from HTMLgen import *
import HTMLcolors as HTMLcolors
import time, biner

           
clefs_r1=['nom','BOS/MTL','WAS/NYR','NJ/CAR','PIT/PHI','SJ/ANA','DET/CLS','VAN/STL','CHI/CAL']
r1=[]
r1.append(['Travis*','BOS 6','NYR 7','NJ 7','PIT 7','SJ 6','DET 6','VAN 6','CAL 4'])
r1.append(['Helene*','BOS 5','NYR 6','NJ 6','PHI 5','ANA 4','DET 4','STL 4','CHI 5'])
r1.append(['David*','BOS 6','WAS 5','CAR 6','PIT 5','SJ 5','DET 4','VAN 7','CAL 6'])
r1.append(['Ross*','BOS 5','NYR 7','NJ 6','PHI 7','SJ 7','DET 6','VAN 6','CHI 6'])
r1.append(['Chee','MTL 6','WAS 5','NJ 7','PIT 6','SJ 6','DET 5','VAN 7','CHI 5'])
r1.append(['Louis-Philippe*','BOS 4','WAS 7','CAR 6','PIT 6','SJ 7','DET 5','VAN 6','CAL 7'])
r1.append(['Simon*','BOS 6','NYR 7','NJ 6','PIT 6','ANA 6','DET 5','VAN 5','CAL 6'])
r1.append(['Dominique*','MTL 7','NYR 6','NJ 7','PHI 6','SJ 6','DET 7','VAN 6','CHI 7'])
r1.append(['Michel*','BOS 5','WAS 7','CAR 6','PHI 6','SJ 6','DET 5','STL 6','CHI 7'])
r1.append(['Phil','BOS 6','WAS 6','NJ 6','PIT 6','SJ 6','DET 5','VAN 6','CHI 6'])
r1.append(['Angelo*','MTL 6','WAS 5','NJ 5','PIT 7','SJ 5','DET 4','VAN 6','CAL 6'])
r1.append(['Seb*','MTL 7','WAS 6','CAR 5','PIT 7','SJ 6','DET 5','VAN 6','CAL 6'])
r1.append(['Daf','BOS 6','WAS 6','CAR 6','PIT 6','SJ 6','DET 5','VAN 6','CHI 6'])
r1.append(['Norm','BOS 6','WAS 7','NJ 7','PIT 6','SJ 7','DET 7','VAN 7','CAL 6'])
r1.append(['Anne*','MTL 6','NYR 6','CAR 6','PHI 7','ANA 7','DET 6','VAN 7','CAL 6'])
r1.append(['Fred*','MTL 6','NYR 6','CAR 7','PHI 7','ANA 6','CLS 6','STL 6','CAL 6'])
r1.append(['Mr. Bourque*','BOS 6','WAS 6','CAR 6','PIT 6','SJ 6','DET 6','VAN 6','CHI 6'])
r1.append(['Phil Roy*','BOS 6','WAS 6','NJ 7','PHI 7','SJ 7','DET 6','VAN 5','CHI 7'])
r1.append(['Vicki*','MTL 7','NYR 7','NJ 7','PIT 6','SJ 6','DET 7','VAN 7','CAL 7'])
r1.append(['Mr.Brown Jr.*','MTL 7','WAS 5','NJ 6','PIT 5','SJ 5','DET 4','VAN 7','CAL 6'])
r1.append(['MF*','BOS 4','WAS 4','NJ 5','PIT 6','SJ 4','DET 5','VAN 6','CHI 7'])
r1.append(['Blaise*','MTL 6','WAS 5','NJ 7','PIT 5','ANA 7','DET 5','VAN 5','CAL 6'])
r1.append(['Luc*','BOS 6','WAS 7','NJ 7','PHI 7','SJ 7','DET 6','VAN 6','CHI 6'])
r1.append(['Duane','BOS 5','WAS 5','CAR 6','PIT 6','SJ 5','DET 5','VAN 7','CHI 5'])
r1.append(['Patrick','MTL 7','WAS 6','CAR 6','PIT 5','SJ 5','DET 6','STL 7','CHI 6'])
r1.append(['Eric G.*','BOS 5','WAS 6','NJ 7','PIT 6','SJ 5','DET 5','VAN 6','CAL 6'])



clefs_r2=['nom','VAN/CHI','DET/ANA','BOS/CAR','WAS/PIT']
r2=[]
r2.append(['Travis*','VAN 6','DET 6','BOS 6','PIT 7'])
r2.append(['Helene*','VAN 6','ANA 5','BOS 6','WAS 5'])
r2.append(['David*','VAN 6','DET 4','BOS 6','PIT 6'])
r2.append(['Ross*','CHI 7','ANA 7','CAR 7','WAS 7'])
r2.append(['Chee','CHI 7','DET 5','BOS 6','PIT 6'])
r2.append(['Louis-Philippe*','VAN 5','DET 6','BOS 6','PIT 6'])
r2.append(['Simon','CHI 6','DET 6','BOS 6','PIT 6'])
r2.append(['Dominique*','VAN 6','DET 7','CAR 7','WAS 6'])
r2.append(['Michel*','VAN 7','DET 5','BOS 6','PIT 6'])
r2.append(['Phil','CHI 6','DET 6','BOS 6','WAS 6'])
r2.append(['Angelo*','CHI 7','DET 6','BOS 5','PIT 6'])
r2.append(['Seb*','CHI 6','DET 6','CAR 6','PIT 6'])
r2.append(['Daf','VAN 6','DET 6','CAR 6','PIT 6'])
r2.append(['Norm','VAN 6','DET 7','BOS 5','PIT 6'])
r2.append(['Anne*','VAN 6','ANA 7','BOS 6','PIT 7'])
r2.append(['Fred*','CHI 4','ANA 4','CAR 4','PIT 4'])
r2.append(['Mr. Bourque','VAN 6','DET 6','BOS 6','PIT 6'])
r2.append(['Phil Roy*','VAN 5','DET 7','BOS 7','PIT 6'])
r2.append(['Vicki*','CHI 7','DET 7','BOS 6','PIT 7'])
r2.append(['Mr.Brown Jr.*','VAN 5','DET 7','BOS 6','PIT 6'])
r2.append(['MF*','CHI 7','DET 6','BOS 5','PIT 7'])
r2.append(['Blaise*','VAN 7','DET 4','BOS 4','WAS 7'])
r2.append(['Luc*','VAN 6','DET 7','BOS 6','PIT 7'])
r2.append(['Duane','VAN 5','DET 5','BOS 5','WAS 7'])
r2.append(['Patrick','CHI 6','DET 6','BOS 6','PIT 6'])
r2.append(['Eric G.','CHI 6','DET 6','BOS 5','PIT 6'])


clefs_r3=['nom','PIT/CAR','DET/CHI']
r3=[]
r3.append(['Travis*','PIT 6','CHI 7'])
r3.append(['Helene*','CAR 7','DET 6'])
r3.append(['David*','PIT 7','DET 6'])
r3.append(['Ross*','PIT 6','CHI 7'])
r3.append(['Chee','PIT 5','CHI 6'])
r3.append(['Louis-Philippe*','CAR 7','DET 5'])
r3.append(['Simon','PIT 6','DET 5'])
r3.append(['Dominique*','CAR 7','DET 6'])
r3.append(['Michel*','PIT 6','DET 6'])
r3.append(['Phil','CAR 6','CHI 6'])
r3.append(['Angelo*','PIT 6','DET 6'])
r3.append(['Seb*','PIT 6','CHI 6'])
r3.append(['Daf','PIT 6','DET 5'])
r3.append(['Norm','PIT 6','DET 5'])
r3.append(['Anne*','PIT 7','DET 6'])
r3.append(['Fred*','CAR 4','CHI 4'])
r3.append(['Mr. Bourque','PIT 6','DET 6'])
r3.append(['Phil Roy*','PIT 7','DET 7'])
r3.append(['Vicki*','PIT 7','DET 7'])
r3.append(['Mr.Brown Jr.*','PIT 5','DET 6'])
r3.append(['MF*','CAR 6','DET 7'])
r3.append(['Blaise*','PIT 7','CHI 7'])
r3.append(['Luc*','PIT 6','DET 7'])
r3.append(['Duane','CAR 6','DET 5'])
r3.append(['Patrick','PIT 7','DET 5'])
r3.append(['Eric G.','PIT 6','CHI 7'])

clefs_r4=['nom','DET/PIT']
r4=[]
r4.append(['Travis*','PIT 6'])
r4.append(['Helene*','DET 7'])
r4.append(['David*','DET 7'])
r4.append(['Ross*','PIT 7'])
r4.append(['Chee','PIT 6'])
r4.append(['Louis-Philippe*','DET 6'])
r4.append(['Simon','DET 6'])
r4.append(['Dominique*','DET 6'])
r4.append(['Michel*','PIT 6'])
r4.append(['Phil','DET 7'])
r4.append(['Angelo*','PIT 4'])
r4.append(['Seb*','DET 6'])
r4.append(['Daf','PIT 6'])
r4.append(['Norm','PIT 7'])
r4.append(['Anne*','DET 7'])
r4.append(['Fred*','PIT 4'])
r4.append(['Mr. Bourque','PIT 6'])
r4.append(['Phil Roy*','PIT 7'])
r4.append(['Vicki*','PIT 6'])
r4.append(['Mr.Brown Jr.*','PIT 5'])
r4.append(['MF*','PIT 6'])
r4.append(['Blaise*','PIT 6'])
r4.append(['Luc*','DET 6'])
r4.append(['Duane','DET 7'])
r4.append(['Patrick','PIT 6'])
r4.append(['Eric G.','PIT 7'])


res_r1={'VAN/STL':'VAN 4','BOS/MTL':'BOS 4','DET/CLS':'DET 4','PIT/PHI':'PIT 6','SJ/ANA':'ANA 6','CHI/CAL':'CHI 6','NJ/CAR':'CAR 7','WAS/NYR':'WAS 7'}
res_r2={'VAN/CHI':'CHI 6','WAS/PIT':'PIT 7','DET/ANA':'DET 7','BOS/CAR':'CAR 7'}
res_r3={'PIT/CAR':'PIT 4','DET/CHI':'DET 5'}
res_r4={'DET/PIT':'PIT 7'}
res=[res_r1,res_r2,res_r3,res_r4]
pts_gagnant=[10,15,20,25]
pts_matchs=[2,3,4,5]

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
#	choix=r1[j]+r2_modif[j]+r3_modif[j]+r4_modif[j]
	choix=r1[j]
	if len(r2_modif) : choix=choix+r2_modif[j]
	if len(r3_modif) : choix=choix+r3_modif[j]
	if len(r4_modif) : choix=choix+r4_modif[j]

	ronde.append(choix)

# On bati le dict des choix de tout le monde
choix=[]
for j in range(len(ronde)) :
	###choix.append(dict(zip(clefs_r1,r1[j])))
	choix.append(dict(zip(clefs,ronde[j])))

##################################################
# on ecrit un petit tableau des choix	

l=''
for c in clefs_r1 : l=l+"%10s" % c
print l

for j in range(len(r1)) :
	l=''
	for c in clefs_r1 :
	 	cc=choix[j][c]
		l=l+"%10s" % cc
	print l

##################################################
# calcul des points

classement=[]
clefs_classement=['nom','ronde 1','ronde 2','demie-finale','finale','total']

# on boucle sur les participants
for p in choix :
	pts=[0,0,0,0]
	# boucle sur les choix
	for c in p.keys() :
		if c != 'nom' :
			# trouver la ronde du choix
			ronde=0
			if c in res_r1 : ronde=1
			elif c in res_r2 : ronde=2
			elif c in res_r3 : ronde=3
			elif c in res_r4 : ronde=4
			#else :
			#print 'serie ',c,' pas finie'
			if ronde != 0 :
				cc=p[c]
				print 'cc=',cc
				choix_g,choix_m=string.split(cc)
				choix_g=string.strip(choix_g)
				choix_m=int(choix_m)
				resultat=res[ronde-1][c]
				res_g,res_m=string.split(resultat)
				res_g=string.strip(res_g)
				res_m=int(res_m)
				print 'nom=',p['nom']
				print 'choix=',choix_g,choix_m
				print 'res=',res_g,res_m
				if choix_g == res_g :
				        print 'bon g'
					pts[ronde-1]=pts[ronde-1]+pts_gagnant[ronde-1]
#					if choix_m == res_m :
#						print 'bon m'
#						pts[ronde-1]=pts[ronde-1]+pts_matchs[ronde-1]
				if choix_m == res_m :
					print 'bon m'
					pts[ronde-1]=pts[ronde-1]+pts_matchs[ronde-1]
	# fin boucle sur les choix
	# on ajoute la ligne au classement
	val=[p['nom'],pts[0],pts[1],pts[2],pts[3],sum(pts)]
	classement.append(dict(zip(clefs_classement,val)))
# fin boucle sur les participants

# classement du classement par le total
classement=biner.classe_liste_dict(classement,'total',-1)

print classement


##################################################
# on genere la page web des choix

page_choix=SimpleDocument('zp2009rc.html')


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
texte.append(Font('Ze Pool 2009',color=HTMLcolors.RED,size='+2'))
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
liste.append("Cette annee, l'heure est grave! Nous avons failli avoir un Ze Pool sans Canadien!!! Profitons-en, ca risque de ne pas durer.")
liste.append("Une autre annee, une autre serie Canadiens/Boston et un autre site Ze Pool identique a ceux des annees precedentes. Comme d'habitude, un * a cote de votre nom indique que vous avez paye votre 5$. Bonnes series.")
liste.append("Record de participation : 26")
page_choix.append(liste)

texte=Text("Treve de billevesees, place a l'action:")
page_choix.append(texte)

#page_choix.append(texte)
page_choix.append(HR())



# on prepare la liste de liens
liste_liens=List()

##################################################
# page des resultats
page_res=SimpleDocument('zp2009rc.html')
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
		for s in r.keys() :
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
page_classement=SimpleDocument('zp2009rc.html')
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

page_r1=SimpleDocument('zp2009rc.html')
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
page_regle=SimpleDocument('zp2009rc.html')
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

				  
