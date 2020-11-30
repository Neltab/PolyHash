#from polyhash.polyhutils.groupBy import Arm

#Création d'un fichier à soumettre
def CreateFile(bras: list):
    with open("output.out", "w") as fichier:
        fichier.write(str(len(bras))+"\n")
        total = 0
        for i in bras:
            total += i.points
            fichier.write(str(i.pm[0])+" "+str(i.pm[1])+" "+str(len(i.taches))+" "+str(len(i.movements))+"\n")
            for y in range(len(i.tachesIndices)):
                fichier.write(str(i.tachesIndices[y])+" ")
            fichier.write("\n")
            for j in range(len(i.movements)):
                fichier.write(i.movements[j]+" ")
            fichier.write("\n")
        print(total)
            



