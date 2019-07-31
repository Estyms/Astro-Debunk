import codecs
import unidecode
from name import Name
import json
import csv
import matplotlib.pyplot as plot

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

file = codecs.open("prenom.txt","r", "utf-8")
file2 = codecs.open("Classement.json","w+","utf-8")
a = file.readlines()
liste = []

for line in a:
    test = unidecode.unidecode(line).replace("\n","").replace("\r","")
    if '' in test or len(test)==0:
        continue
    else:
        name = Name(test.capitalize())
        name.calc()
        liste.append(name)

liste.sort(key=lambda x: x.score, reverse=True)

dictio = {}
plotdic = {
    "Pas Très Sexy":0,
    "Assez Sexy":0,
    "Très Sexy":0,
    "Le Plus Sexy":0
}
perc = {}

j = 0
currentScore = 0
for i in liste:
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

perc["Le Plus Sexy"] = (plotdic["Le Plus Sexy"] / len(liste))*100
perc["Très Sexy"] = (plotdic["Très Sexy"] / len(liste))*100
perc["Assez Sexy"] = (plotdic["Assez Sexy"] / len(liste))*100
perc["Pas Très Sexy"] = (plotdic["Pas Très Sexy"] / len(liste))*100

colors = ['red', 'green', 'orange', 'blue']

labels = [
    "Le Plus Sexy " + str(perc["Le Plus Sexy"])[0:5] + "%\nEffectif : " + str(plotdic["Le Plus Sexy"]),
    "Très Sexy " + str(perc["Très Sexy"])[0:5] + "%\nEffectif : " + str(plotdic["Très Sexy"]),
    "Assez Sexy " + str(perc["Assez Sexy"])[0:5] + "%\nEffectif : " + str(plotdic["Assez Sexy"]),
    "Pas Très Sexy " + str(perc["Pas Très Sexy"])[0:5] + "%\nEffectif : " + str(plotdic["Pas Très Sexy"])
    ]
print(labels)
patches, text = plot.pie(list(perc.values()), colors=colors, startangle=90)
plot.gcf().set_facecolor("#15202b")
plot.axis("equal")
plot.legend(patches,labels,loc='best')
plot.tight_layout()


plot.show()

file2.write(json.dumps(dictio, indent=4))

        