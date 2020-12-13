#from polyhash.polyhutils.groupBy import Arm

#Création d'un fichier à soumettre
def CreateFile(bras: list):
    with open("output.txt", "w") as fichier:
        fichier.write(str(len(bras))+"\n")
        for i in bras:
            fichier.write(str(i.pm[0])+" "+str(i.pm[1])+" "+str(len(i.taches))+" "+str(i.etapes)+"\n")
            for y in range(len(i.tachesIndices)):
                fichier.write(str(i.tachesIndices[y])+" ")
            fichier.write("\n")
            for j in range(len(i.movements)):
                fichier.write(i.movements[j]+" ")
            fichier.write("\n")

            



