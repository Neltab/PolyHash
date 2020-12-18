def CreateFile(bras: list, nomFichier: str):
    """ Création du fichier de sortie en fonction des paramètres fournis dans la liste de bras

    :param bras: Liste des bras créés par le programme    
    """

    with open("./output_files/" + nomFichier + ".out", "w") as fichier:
        # On écrit le nombre de bras à utiliser
        fichier.write(str(len(bras))+"\n")
        total = 0

        # Pour chaque bras on va écrire 4 lignes :
        # Coordonnées du point de montage, nombre de tâches et nombres de mouvements
        # Liste des indices des tâches à effectuer
        # Liste des mouvements
        # Ligne vide de séparation
        for i in bras:
            for task in i.taskDone:
                total += task.nbpoint
            fichier.write(str(i.pm[0])+" "+str(i.pm[1])+" "+str(len(i.taskDone))+" "+str(len(i.movementsDone))+"\n")
            for y in range(len(i.taskDone)):
                fichier.write(str(i.taskDone[y].indice)+" ")
            fichier.write("\n")
            for j in range(len(i.movementsDone)):
                fichier.write(i.movementsDone[j]+" ")
            fichier.write("\n")
