
from HTMLgen.HTMLgen import *
import HTMLgen.HTMLcolors as HTMLcolors
import time, biner

           
clefs_r1=['nom','OTT/TB','CAR/MTL','NJ/NYR','BUF/PHI','DET/EDM','DAL/COL','CAL/ANA','NAS/SJ']
r1=[]
r1.append(['Phil','OTT 6','CAR 6','NJ 5','BUF 6','DET 5','DAL 5','CAL 7','SJ 6'])
r1.append(['Daf','OTT 5','CAR 5','NJ 5','BUF 5','DET 5','DAL 5','CAL 5','SJ 6'])
r1.append(['Dominique','OTT 6','MTL 7','NJ 7','PHI 7','DET 6','COL 7','CAL 7','SJ 7'])
r1.append(['Eric C','OTT 5','MTL 7','NJ 6','BUF 7','DET 4','DAL 6','CAL 6','SJ 5'])
r1.append(['Travis','OTT 7','CAR 6','NJ 6','BUF 7','EDM 7','DAL 5','CAL 7','SJ 6'])
r1.append(['Dorothee','OTT 5','MTL 7','NJ 6','BUF 6','DET 4','DAL 6','CAL 6','NAS 5'])
r1.append(['Biner','TB 7','MTL 6','NJ 5','BUF 6','DET 5','DAL 6','CAL 5','SJ 6'])
r1.append(['Louis-philippe','OTT 6','CAR 4','NJ 5','BUF 5','DET 5','DAL 6','CAL 7','SJ 6'])
r1.append(['Eric G','OTT 6','CAR 5','NJ 6','BUF 6','DET 4','DAL 5','CAL 6','SJ 6'])
r1.append(['El Dictator JFC','OTT 5','CAR 5','NJ 6','BUF 7','DET 5','DAL 6','CAL 6','SJ 6'])
r1.append(['Fred','OTT 6','CAR 6','NYR 6','BUF 7','DET 6','DAL 6','CAL 6','NAS 7'])
r1.append(['Mr. Bourque','OTT 6','CAR 6','NJ 7','BUF 7','DET 5','DAL 5','CAL 7','SJ 6'])
r1.append(['Simon','OTT 5','CAR 5','NJ 7','BUF 6','DET 4','DAL 6','CAL 6','SJ 5'])
r1.append(['Normand','OTT 7','CAR 6','NJ 5','BUF 5','DET 4','DAL 6','CAL 6','SJ 6'])
r1.append(['Olivier','OTT 6','CAR 6','NJ 6','BUF 5','DET 5','DAL 5','CAL 6','SJ 6'])
r1.append(['Isabelle','OTT 6','MTL 6','NJ 5','BUF 7','DET 5','COL 6','CAL 6','SJ 6'])
r1.append(['Christophe','OTT 6','CAR 6','NYR 7','PHI 7','DET 4','DAL 5','CAL 6','SJ 7'])

#clefs_r2=['nom','TB/MTL','PHI/TOR','DET/CAL','SJ/COL']
clefs_r2=['nom','OTT/BUF','CAR/NJ','SJ/EDM','ANA/COL']
r2=[]
r2.append(['Phil','BUF 7','NJ 6','SJ 6','ANA 6'])
r2.append(['Daf','OTT 6','NJ 5','EDM 6','COL 6'])
r2.append(['Dominique','BUF 6','NJ 6','SJ 6','COL 6'])
r2.append(['Eric C','OTT 6','NJ 5','SJ 7','COL 6'])
r2.append(['Travis','OTT 6','CAR 7','EDM 7','COL 6'])
r2.append(['Dorothee','OTT 6','NJ 5','EDM 7','COL 7'])
r2.append(['Biner','BUF 7','NJ 5','EDM 6','COL 6'])
r2.append(['Louis-philippe','BUF 7','NJ 5','SJ 6','COL 6'])
r2.append(['Eric G','OTT 7','CAR 7','SJ 7','ANA 7'])
r2.append(['El Dictator JFC','OTT 6','NJ 6','SJ 6','COL 6'])
r2.append(['Fred','BUF 6','CAR 5','EDM 6','ANA 7'])
r2.append(['Mr. Bourque','OTT 7','NJ 5','SJ 5','ANA 6'])
r2.append(['Simon','BUF 6','NJ 6','EDM 7','COL 6'])
r2.append(['Normand','OTT 6','NJ 5','SJ 6','COL 6'])
r2.append(['Olivier','OTT 6','NJ 6','SJ 6','COL 6'])
r2.append(['Isabelle','BUF 7','NJ 5','EDM 7','COL 6'])
r2.append(['Christophe','OTT 5','CAR 6','EDM 5','COL 6'])

clefs_r3=['nom','CAR/BUF','ANA/EDM']
r3=[]
r3.append(['Phil','BUF 6','ANA 6'])
r3.append(['Daf','BUF 6','EDM 6'])
r3.append(['Dominique','CAR 6','ANA 6'])
r3.append(['Eric C','BUF 5','EDM 5'])
r3.append(['Travis','BUF 6','EDM 7'])
r3.append(['Dorothee','BUF 6','EDM 7'])
r3.append(['Biner','BUF 6','EDM 7'])
r3.append(['Louis-philippe','CAR 6','ANA 6'])
r3.append(['Eric G','BUF 6','EDM 6'])
r3.append(['El Dictator JFC','CAR 6','EDM 6'])
r3.append(['Fred','CAR 6','EDM 6'])
r3.append(['Mr. Bourque','CAR 7','ANA 6'])
r3.append(['Simon','BUF 6','EDM 7'])
r3.append(['Normand','CAR 7','EDM 6'])
r3.append(['Olivier','CAR 7','ANA 7'])
r3.append(['Isabelle','CAR 6','EDM 6'])
r3.append(['Christophe','CAR 7','EDM 6'])

#clefs_r4=['nom','TB/CAL']
clefs_r4=['nom','CAR/EDM']
r4=[]
r4.append(['Phil','CAR 6'])
r4.append(['Daf','EDM 6'])
r4.append(['Dominique','CAR 7'])
r4.append(['Eric C','EDM 6'])
r4.append(['Travis','EDM 6'])
r4.append(['Dorothee','EDM 6'])
r4.append(['Biner','EDM 5'])
r4.append(['Louis-philippe','CAR 6'])
r4.append(['Eric G','CAR 4'])
r4.append(['El Dictator JFC','CAR 5'])
r4.append(['Fred','CAR 5'])
r4.append(['Mr. Bourque','CAR 7'])
r4.append(['Simon','EDM 6'])
r4.append(['Normand','CAR 7'])
r4.append(['Olivier','CAR 6'])
r4.append(['Isabelle','EDM 6'])
r4.append(['Christophe','CAR 6'])

#r4.append(['chenard','TB 7'])

res_r1={'OTT/TB':'OTT 5','NJ/NYR':'NJ 4','DET/EDM':'EDM 6','DAL/COL':'COL 5','NAS/SJ':'SJ 5','BUF/PHI':'BUF 6','CAR/MTL':'CAR 6','CAL/ANA':'ANA 7'}
res_r2={'ANA/COL':'ANA 4','CAR/NJ':'CAR 5','OTT/BUF':'BUF 5','SJ/EDM':'EDM 6'}
res_r3={'ANA/EDM':'EDM 5','CAR/BUF':'CAR 7'}
res_r4={'CAR/EDM':'CAR 7'}
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

page_choix=SimpleDocument('zp2006rc.html')


# on prepare le lien vers l'entete
page_choix.append(Name('entete'))
lien_entete=Href('#entete',Font('retour en haut',size='-1'))

# affichage de la derniere mise a jour
texte_widget=RawText('<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,29,0" width="158" height="140"><param name="movie"value="nameofwidget.swf"><param name="wmode" value="transparent"><param name=quality value=high><embed src="canadienspresentaway.swf" quality=high pluginspage="http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash" type="application/x-shockwave-flash" width="158" height="140" wmode="transparent"></embed></object>')
font_maj=Font(size='0')
#texte_maj='derniere mise a jour:'+time.strftime('%d/%m/%Y',time.localtime())
texte_maj=Text('derniere mise a jour:')
texte_maj.append(texte_widget)
texte_maj.append(time.strftime('/%m/%Y',time.localtime()))

font_maj.append(texte_maj)
page_choix.append(Paragraph(font_maj,align='right'))




texte=Text()
coupe=Image('images/stanleycup.jpg',width=50)
texte.append(coupe)
texte.append(Font('Ze Pool 2006',color=HTMLcolors.RED,size='+2'))
texte.append(coupe)
page_choix.append(Heading(1,texte,align='center'))

texte=Text()
texte.append("Bienvenue sur la page officielle du pool des series de la coupe Stanley de la communaute OURANOS-SCA/UQAM-EC")
page_choix.append(Heading(2,texte))

texte=Text()
pdaj=Image('images/pdagenais.jpg')
texte.append(BR())
texte.append(pdaj)
texte.append("un site dedie a Pierre Dagenais, le plus fin marqueur du CH depuis des lunes")
texte.append(P())
page_choix.append(texte)
page_choix.append(HR())



# on prepare la liste de liens
liste_liens=List()

##################################################
# page des resultats
page_res=SimpleDocument('zp2006rc.html')
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
page_classement=SimpleDocument('zp2006rc.html')
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

page_r1=SimpleDocument('zp2006rc.html')
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
page_regle=SimpleDocument('zp2006rc.html')
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

# inclusion de la musique

#<embed SRC=hockey.wav AUTOPLAY=true AUTOSTART=true HIDDEN=true LOOP=false height="50"
#width="200" >
musique=Embed(src='wav/hockey.wav',autoplay='true',autostart='true',hidden='true',loop='false',height=50,width=50)

#ecriture de la page

page_choix.append(musique)
page_choix.append(liste_liens)
page_choix.append(page_res)
page_choix.append(page_classement)
page_choix.append(page_r1)
page_choix.append(page_regle)
page_choix.write('index.html')

				  
