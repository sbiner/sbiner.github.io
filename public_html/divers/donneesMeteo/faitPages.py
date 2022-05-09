from HTMLgen.HTMLgen import *
import HTMLgen.HTMLcolors as HTMLcolors

listeVille=['MTL','STHUB','QC']
listeVar=['precip','temperature','neige','neigeAuSol']
listeNbJours=['010','030','100','180','365']


class PageType(SimpleDocument) :
    bgcolor=HTMLcolors.YELLOW

def fait_page(nomVille,nomVar,nbJours) :
    p=PageType()
    
    # ajout des villes
    t=Text()
    for autreVille in listeVille :
        lien=Href(autreVille+'_'+nomVar+'_'+nbJours+'.html',autreVille)
        t.append(lien)
        t.append(' ')
    t.append(BR())
    p.append(t)
    
    # ajout des variables
    t=Text()
    for autreVar in listeVar :
        lien=Href(nomVille+'_'+autreVar+'_'+nbJours+'.html',autreVar)
        t.append(lien)
        t.append(' ')
    t.append(BR())
    p.append(t)
    
    # ajout des nombres de jours
    t=Text()
    for autreNbJours in listeNbJours :
        lien=Href(nomVille+'_'+nomVar+'_'+autreNbJours+'.html',autreNbJours)
        t.append(lien)
        t.append(' ')
    t.append(BR())
    p.append(t)
    
    # ajout de la figure
    
    repImage='fig/'+nomVille
    fig=Image('fig/'+nomVille+'/'+nomVar+'_'+nbJours+'j.png',align='center')
    p.append(fig)
    
    # ecriture de la page
    
    p.write(nomVille+'_'+nomVar+'_'+nbJours+'.html')

    
if __name__ == '__main__' :
    for nomVille in listeVille :
        for nomVar in listeVar :
            for nbJours in listeNbJours :
                fait_page(nomVille,nomVar,nbJours)

