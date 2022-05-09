from HTMLgen.HTMLgen import *
import HTMLgen.HTMLcolors as HTMLcolors

class PageType(SimpleDocument) :
    bgcolor=HTMLcolors.YELLOW

def fait_page_index() :
    p=PageType()
    p.append(Heading(2,'Divers'))
    texte=Emphasis("Voici quelques liens menant a differents petits projets que j'ai realises au fil des ans")
    p.append(texte)
    
    menu_divers=List()
    lien=Href("ze_pool/index.html",'Ze Pool',target='affichage')
    t=Text()
    t.append(lien)
    t.append(", pool que j'organise pour les series de la Stanley.")
    menu_divers.append(t)
    
    t=Text()
    lien=Href("poolYahoo/index.html",'Bainerz Cup')
    t.append(lien)
    t.append(', pool de la saison reguliere sur Yahoo!')
    menu_divers.append(t)
    
    t=Text()
    lien=Href("donneesMeteo/index.html",'affichage des donnees meteorologiques')
    t.append(lien)
    t.append(' recentes comparees aux dernieres annees et a la climatologie')
    menu_divers.append(t)
    
    p.append(menu_divers)

    p.write('index.html')
    
    
if __name__ == '__main__' :
    fait_page_index() 
