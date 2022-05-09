from HTMLgen.HTMLgen import *
import HTMLgen.HTMLcolors as HTMLcolors

class PageType(SimpleDocument) :
    bgcolor=HTMLcolors.YELLOW

def fait_page_index() :

    f1=Frame(src="menu_gauche.html")
    f2=Frame(name="affichage",scrolling="auto", src="accueil.html")
    fs=Frameset(f1,f2,cols='200,*')
    fsdoc=FramesetDocument()
    fsdoc.append(fs)
    fsdoc.write('index.html')

def fait_menu_gauche() :
    t=TableLite()
    liste_nom=['acceuil','coordonnees','CV (a venir)','publications (a venir)','divers','perso (acces restreint)']
    liste_liens=['accueil.html','coord.html','','','divers/index.html','']
    for i in range(len(liste_nom)):
	ligne=TR()
	texte=liste_nom[i]
	lien=liste_liens[i]
	if lien == '' :
	    ligne.append(TD(texte))
	else :
	    lien=Href(url=lien,text=texte,target="affichage")
	    ligne.append(TD(lien))
	t.append(ligne)
    p=SimpleDocument(bgcolor=HTMLcolors.CADETBLUE)
    p.append(t)
    p.write('menu_gauche.html')

def fait_accueil() :
    p=PageType()
    p.append(Heading(2,'La Page Web de Seb',align='centre'))
    p.append(Image('images/biner_tux_1.jpg',width=180))
    t=Text()
    t.append(P())
    t.append(
	"""
	Bonjour, je m'appelle Sébastien Biner et ceci est ma page web. Je
	suis un joyeux luron spécialiste en simulation climatique au
	consortium Ouranos, organisateur occasionnel de pool de hockey,
	père de trois charmants enfants, Ëtre humain et bien d'autres choses encore.
	"""
	)
    t.append(P())
    t.append(
	"""
	Ces différentes occupations m'ont amené à créer ce site afin de
	pouvoir partager des pages web et a rendre disponible des informations a mon sujet.
	"""
	)
    t.append(P())
    t.append(
	"""
	Bonne navigation!     
	"""
	)
    t.append(P())

    p.append(t)

    p.write('accueil.html')
    
def fait_coord() :
    p=PageType()
    p.append(Heading(2,'Coordonnees'))
    p.append(HR())

    l=TR()
    l.append(TD(Strong('Travail:'),valign='top'))
    t=Text()
    t.append('Ouranos')
    t.append(BR())
    t.append('550 Sherbrook ouest, 19e etage')
    t.append(BR())
    t.append('Montreal, PQ')
    t.append(BR())
    t.append('Canada')
    t.append(BR())
    t.append('H3A 1B9')
    t.append(BR())
    t.append(BR())
    t.append('tel: 514.282.6464 poste 263')
    t.append(BR())
    t.append('fax: 514.282.7131')
    t.append(BR())
    l.append(TD(t))
    table=TableLite()
    table.append(l)
    p.append(table)
    p.append(HR())

    l=TR()
    l.append(TD(Strong('Maison:'),valign='top'))
    t=Text()
    t.append('285 Merton')
    t.append(BR())
    t.append('St-Lambert, PQ')
    t.append(BR())
    t.append('Canada')
    t.append(BR())
    t.append('J4P 2W4')
    t.append(BR())
    t.append(BR())
    t.append('tel: 450.466.9182')
    l.append(TD(t))
    table=TableLite()
    table.append(l)
    p.append(table)

    p.append(HR())
    l=TR()
    l.append(TD(' '))
    l.append(TD('biner.sebastien@ouranos.ca'))
    t=TableLite()
    t.append(l)
    p.append(t)
    
    
    p.write('coord.html')
	     


def main() :
    fait_page_index()
    fait_menu_gauche()
    fait_accueil()
    fait_coord()


if __name__ == '__main__' : main()
