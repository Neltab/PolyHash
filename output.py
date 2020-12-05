#from polyhash.polyhutils.groupBy import Arm

#Création d'un fichier à soumettre
def CreateFile(bras: list):
    with open("output_d-2.out", "w") as fichier:
        fichier.write(str(len(bras))+"\n")
        total = 0
        debug1 = 62
        debug2 = 35
        for i in bras:
            for task in i.taskDone:
                total += task.nbpoint
            fichier.write(str(i.pm[0])+" "+str(i.pm[1])+" "+str(len(i.taskDone))+" "+str(len(i.movementsDone))+"\n")
            for y in range(len(i.taskDone)):
                fichier.write(str(i.taskDone[y].indice)+" ")
            fichier.write("\n")
            for j in range(len(i.movementsDone)):
                if i.movementsDone[j] == "L":
                    debug1 -= 1
                elif i.movementsDone[j] == "R":
                    debug1 += 1
                elif i.movementsDone[j] == "U":
                    debug2 += 1
                elif i.movementsDone[j] == "D":
                    debug2 -= 1
                
                if j == 3362:
                    print([debug1,debug2])

                fichier.write(i.movementsDone[j]+" ")
            fichier.write("\n")
        print(total)
            



