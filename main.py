#Modules
import codecs
import unidecode
from name import Name
import json
import matplotlib.pyplot as plot

#Ouverture et lecture des fichiers
prenoms = codecs.open("prenom.txt","r", "utf-8")
classement = codecs.open("Classement.json","w+","utf-8")
linesPrenoms = prenoms.readlines()

#Importation des prénoms dans une liste à partir du fichier prenom.txt
nameList = []
for line in linesPrenoms:
    decodedName = unidecode.unidecode(line).replace("\n","").replace("\r","")
    name = Name(decodedName.capitalize())
    name.calc()
    nameList.append(name)

#Tri par score de la liste des prénoms
nameList.sort(key=lambda x: x.score, reverse=True)

#Création du classement pour chacun des prénoms

dictio = {}

plotdic = {
    "Pas Très Sexy":0,
    "Assez Sexy":0,
    "Très Sexy":0,
    "Le Plus Sexy":0
}


j = 0
currentScore = 0
for i in nameList:
    if i.score != currentScore: 
        j = j + 1
        currentScore = i.score

    if i.score < 60:
        plotdic["Pas Très Sexy"] = plotdic["Pas Très Sexy"] + 1
    elif i.score < 300:
        plotdic["Assez Sexy"] = plotdic["Assez Sexy"] + 1
    elif i.score < 600:
        plotdic["Très Sexy"] = plotdic["Très Sexy"] + 1
    else:
        plotdic["Le Plus Sexy"] = plotdic["Le Plus Sexy"] + 1
    dictio[i.name] = {
        "classement":j,
        "score":i.score}

#Écriture du classement dans un fichier json 
classement.write(json.dumps(dictio, indent=4))

#Calcul des pourcentage de chacune des catégories
perc = {}

perc["Le Plus Sexy"] = (plotdic["Le Plus Sexy"] / len(nameList))*100
perc["Très Sexy"] = (plotdic["Très Sexy"] / len(nameList))*100
perc["Assez Sexy"] = (plotdic["Assez Sexy"] / len(nameList))*100
perc["Pas Très Sexy"] = (plotdic["Pas Très Sexy"] / len(nameList))*100

#Création du fichier stat
colors = ['red', 'green', 'orange', 'blue']

labels = [
    "Le Plus Sexy " + str(perc["Le Plus Sexy"])[0:5] + "%\nEffectif : " + str(plotdic["Le Plus Sexy"]),
    "Très Sexy " + str(perc["Très Sexy"])[0:5] + "%\nEffectif : " + str(plotdic["Très Sexy"]),
    "Assez Sexy " + str(perc["Assez Sexy"])[0:5] + "%\nEffectif : " + str(plotdic["Assez Sexy"]),
    "Pas Très Sexy " + str(perc["Pas Très Sexy"])[0:5] + "%\nEffectif : " + str(plotdic["Pas Très Sexy"])
    ]

patches, text = plot.pie(list(perc.values()), colors=colors, startangle=90)
plot.gcf().set_facecolor("#15202b")
plot.axis("equal")
plot.legend(patches,labels,loc='best')
plot.tight_layout()

#Affichage du diagramme
plot.show()