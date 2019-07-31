#Module
import re

#Création de la classe Name
class Name:
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.parsedName = ''
        
        #Score de chacune des lettres
        self.dic = {
                'a':100,
                'b':14,
                'c':9,
                'd':28,
                'e':145,
                'f':12,
                'g':3,
                'h':10,
                'i':200,
                'j':100,
                'k':114,
                'l':100,
                'm':25,
                'n':450,
                'o':80,
                'p':2,
                'q':12,
                'r':400,
                's':113,
                't':405,
                'u':11,
                'v':10,
                'w':10,
                'x':3,
                'y':210,
                'z':23,
                ' ':0
            }
    
    #Calcul des points du prénom
    def calc(self):
        name = self.name.lower()
        name = name.replace('-'," ").replace('\'', " ")
        self.parsedName += re.sub('[^a-z ]+','',name)
        for char in self.parsedName:
            self.score += self.dic[char]
