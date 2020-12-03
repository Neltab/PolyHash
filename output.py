#from polyhash.polyhutils.groupBy import Arm

#Création d'un fichier à soumettre
def CreateFile(bras: list):
    with open("output.out", "w") as fichier:
        fichier.write(str(len(bras))+"\n")
        total = 0
        for i in bras:
            total += i.points
            fichier.write(str(i.pm[0])+" "+str(i.pm[1])+" "+str(len(i.taskDone))+" "+str(len(i.movementsDone))+"\n")
            for y in range(len(i.tachesIndices)):
                fichier.write(str(i.taskDone[y].indice)+" ")
            fichier.write("\n")
            for j in range(len(i.movementsDone)):
                fichier.write(i.movementsDone[j]+" ")
            fichier.write("\n")
        print(total)
            



