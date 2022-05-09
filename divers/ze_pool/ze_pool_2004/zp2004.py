from HTMLgen import *
import HTMLcolors, time, biner

           
clefs_r1=['nom','TB/NYI','BOS/MTL','PHI/NJ','TOR/OTT','DET/NAS','SJ/STL','VAN/CAL','COL/DAL']
r1=[]
r1.append(['chenard','TB 5','MTL 6','NJ 5','OTT 7','DET 4','SJ 6','CAL 7', 'COL 7'])
r1.append(['girard','TB 6','MTL 7','NJ 5','OTT 7','DET 5','SJ 6','VAN 7','DAL 6'])
r1.append(['phil','TB 5','BOS 6','NJ 6','TOR 6','DET 5','STL 6','CAL 7','COL 7'])
r1.append(['lam','TB 7','MTL 6','PHI 7','TOR 5','DET 6','SJ 6','CAL 7','DAL 7'])
r1.append(['seb','TB 5','MTL 6','PHI 6','TOR 7','DET 5','SJ 6','CAL 6','COL 6'])
r1.append(['Mr. bourque','TB 6','BOS 7','NJ 6','TOR 7','DET 5','SJ 7','CAL 6','DAL 6'])
r1.append(['mike','TB 7','MTL 6','NJ 6','TOR 7','DET 4','SJ 5','VAN 6','COL 7'])
r1.append(['norm','TB 7','MTL 7','NJ 6','TOR 7','DET 6','STL 6','CAL 6','DAL 7'])
r1.append(['liby','TB 6','MTL 7','NJ 6','TOR 7','DET 5','STL 6','VAN 7','COL 6'])
r1.append(['rene','TB 5','MTL 7','NJ 6','TOR 7','DET 5','SJ 5','VAN 6','DAL 5'])
r1.append(['alain beaulne','TB 6','MTL 6','PHI 7','OTT 7','DET 6','STL 7','VAN 6','COL 6'])
r1.append(['JF','TB 6','MTL 6','NJ 6','TOR 6','DET 5','SJ 6','VAN 7','DAL 6'])
r1.append(['Nicolas','TB 6','BOS 6','NJ 6','TOR 7','DET 4','STL 7','CAL 6','DAL 6'])
r1.append(['Olivier','TB 6','MTL 7','NJ 6','TOR 6','DET 6','SJ 6','VAN 7','DAL 6'])

clefs_r2=['nom','TB/MTL','PHI/TOR','DET/CAL','SJ/COL']
r2=[]
r2.append(['chenard','MTL 6','TOR 7','DET 5','COL 6'])
r2.append(['girard','MTL 6','PHI 6','DET 6','COL 6'])
r2.append(['phil','MTL 7','TOR 6','CAL 7','COL 6'])
r2.append(['lam','MTL 5','PHI 6','DET 7','SJ 7'])
r2.append(['seb','MTL 6','TOR 6','CAL 6','SJ 6']) 
r2.append(['Mr. Bourque','MTL 6','PHI 5','DET 5','COL 7'])
r2.append(['mike','MTL 6','PHI 6','DET 7','COL 7'])
r2.append(['norm','MTL 6','PHI 7','DET 5','COL 6'])
r2.append(['liby','MTL 7','TOR 7','CAL 7','COL 6'])
r2.append(['rene','MTL 6','PHI 6','CAL 7','COL 6'])
r2.append(['alain beaulne','MTL 7','PHI 7','DET 6','COL 6'])
r2.append(['JF','TB 6','PHI 7','DET 6','COL 6'])
r2.append(['Nicolas','MTL 6','PHI 7','CAL 6','SJ 7'])
r2.append(['Olivier','MTL 6','PHI 6','CAL 7','SJ 7'])

clefs_r3=['nom','TB/PHI','SJ/CAL']
r3=[]
r3.append(['chenard','TB 6','CAL 6'])
r3.append(['girard','TB 7','SJ 7'])
r3.append(['phil','TB 5','CAL 7'])
r3.append(['lam','PHI 6','SJ 6'])
r3.append(['seb','TB 6','CAL 7'])
r3.append(['Mr. Bourque','PHI 6','SJ 5'])
r3.append(['mike','TB 6','SJ 6'])
r3.append(['norm','TB 6','SJ 7'])
r3.append(['liby','TB 6','CAL 7'])
r3.append(['rene','TB 6','SJ 7'])
r3.append(['alain beaulne','TB 5','CAL 6'])
r3.append(['JF','PHI 6','SJ 6'])
r3.append(['Nicolas','PHI 6','CAL 6'])
r3.append(['Olivier','PHI 6','SJ 6'])

clefs_r4=['nom','TB/CAL']
r4=[]
r4.append(['chenard','TB 7'])
r4.append(['girard','TB 5'])
r4.append(['phil','CAL 7'])
r4.append(['lam','CAL 6'])
r4.append(['seb','CAL 6'])
r4.append(['Mr. Bourque','TB 6'])
r4.append(['mike','CAL 6'])
r4.append(['norm','TB 6'])
r4.append(['liby','CAL 7'])
r4.append(['rene','TB 5'])
r4.append(['alain beaulne','TB 7'])
r4.append(['JF','TB 7'])
r4.append(['Nicolas','TB 7'])
r4.append(['Olivier','TB 7'])

res_r1={'SJ/STL':'SJ 5','TB/NYI':'TB 5','PHI/NJ':'PHI 5','DET/NAS':'DET 6','COL/DAL':'COL 5','BOS/MTL':'MTL 7',
		  'VAN/CAL':'CAL 7','TOR/OTT':'TOR 7'}
res_r2={'TB/MTL':'TB 4','DET/CAL':'CAL 6','PHI/TOR':'PHI 6','SJ/COL':'SJ 6'}
res_r3={'SJ/CAL':'CAL 6','TB/PHI':'TB 7'}
#res_r4={'TB/CAL':'XXX X'}
res_r4={'TB/CAL':'TB 7'}
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
	choix=r1[j]+r2_modif[j]+r3_modif[j]+r4_modif[j]
	ronde.append(choix)

# on bati le dict des choix de tout le monde
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

page_choix=SimpleDocument('zp2004.rc')


# on prepare le lien vers l'entete
page_choix.append(Name('entete'))
lien_entete=Href('#entete',Font('retour en haut',size='-1'))

# affichage de la derniere mise a jour
font_maj=Font(size='-1')
texte_maj='derniere mise a jour:'+time.strftime('%d/%m/%Y',time.localtime())
font_maj.append(texte_maj)
page_choix.append(Paragraph(font_maj,align='right'))

texte=Text()
coupe=Image('images/stanleycup.jpg',width=50)
texte.append(coupe)
texte.append(Font('Ze Pool 2004',color=HTMLcolors.RED,size='+2'))
texte.append(coupe)
page_choix.append(Heading(1,texte,align='center'))

texte=Text()
texte.append("Bienvenue sur la page officielle du pool des series de la coupe Stanley de la communaute OURANOS-SCA/UQAM-EC")

page_choix.append(Heading(2,texte))

# on prepare la liste de liens
liste_liens=List()

##################################################
# page des resultats
page_res=SimpleDocument('zp2004.rc')
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
page_classement=SimpleDocument('zp2004.rc')
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
	texte="%15s" % c
	ligne.append(TH(Font(texte,color=HTMLcolors.RED5)))
t.append(ligne)
# nom des participant et resultats
for i in range(len(classement)) :
	ligne=TR()
	for c in clefs_classement :
		cc=classement[i][c]
		texte="%15s" % cc
		couleur=HTMLcolors.BLACK
		if c == 'nom' : couleur=HTMLcolors.RED5
		ligne.append(TD(Font(texte,color=couleur)))
	t.append(ligne)
# ajout du tableau a la page
page_classement.append(t)

##################################################
# page des choix 

page_r1=SimpleDocument('zp2004.rc')
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
page_regle=SimpleDocument('zp2004.rc')
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
liste.append('le deuximeme recoit 2 fois sa mise.')
liste.append('le troisieme recupere sa mise.')
liste.append('la mise est de 10$ cette annee.')

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


#ecriture de la page

page_choix.append(liste_liens)
page_choix.append(page_res)
page_choix.append(page_classement)
page_choix.append(page_r1)
page_choix.append(page_regle)
page_choix.write('zp4.html')

				  
