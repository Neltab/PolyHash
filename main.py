#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Input2 import GRILLE, BRAS, NBPTDEMONT, NBTACHES, NBETAPES, LPOINTDEMONT, LTASK

from polyhash.Pathfinding.Grid import apply_points_to_grid
from polyhash.Pathfinding.Grid import GenerateNodeGrid
from polyhash.Pathfinding import settings as S, pathfinding
from polyhash.polyhutils.groupBy.Arm import Arm

from polyhash import groupBy

from output import CreateFile

if __name__ == "__main__":

    #####################
    # Partie d'Aurélien #
    #####################

    bras = groupBy.rendement(LTASK, LPOINTDEMONT, BRAS)
    # for b in bras:
    #     print(b.taches[0].coordtask[0], b.taches[1].coordtask[0], b.taches[2].coordtask[0])


    # $ Interface :
    # import tkinter as tk
    # from tkinter import EventType

    # COLORS = ['gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray','light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2','AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3','MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3','SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4','DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2','LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3','SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3','LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3','CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3','cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4','aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2','orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2','MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4']
    # window = tk.Tk()
    # canvas = tk.Canvas(window, width=1000, height=1000)
    # canvas.pack()

    # def do_zoom(event):
    #     factor = 1.001 ** event.delta
    #     canvas.scale(tk.ALL, event.x, event.y, factor, factor)
    # canvas.bind("<MouseWheel>", do_zoom)
    # canvas.bind('<ButtonPress-1>', lambda event: canvas.scan_mark(event.x, event.y))
    # canvas.bind("<B1-Motion>", lambda event: canvas.scan_dragto(event.x, event.y, gain=1))

    # bras = groupBy.rendement(LTASK, LPOINTDEMONT, BRAS)
    # # for b in bras:
    # #     print(b.pm)

    # taille_case = 5
    # color = ["blue","red"]

    # # for pm in LPOINTDEMONT:
    # #     canvas.create_rectangle(pm[0]*taille_case, 1000-pm[1]*taille_case, (pm[0]*taille_case+taille_case), 1000-(pm[1]*taille_case+taille_case), fill="blue", outline='')

    # for t in LTASK:
    #     for coord in t.coordtask:
    #         canvas.create_rectangle(coord[0]*taille_case, 1000-coord[1]*taille_case, (coord[0]*taille_case + taille_case), 1000-(coord[1]*taille_case + taille_case), fill = 'red', outline='')

    # i = 0
    # for b in bras:
    #     canvas.create_rectangle(b.pm[0]*taille_case, 1000-b.pm[1]*taille_case, b.pm[0]*taille_case+taille_case, 1000-(b.pm[1]*taille_case+taille_case), fill=COLORS[i], outline='black')
    #     for task in b.taches:
    #         for coord in task.coordtask:
    #             canvas.create_rectangle(coord[0]*taille_case, 1000-coord[1]*taille_case, (coord[0]*taille_case + taille_case), 1000-(coord[1]*taille_case + taille_case), fill = COLORS[i], outline='')
    #     i += 3

    # b = bras[3]
    # canvas.create_rectangle(b.pm[0]*taille_case, 1000-b.pm[1]*taille_case, b.pm[0]*taille_case+taille_case, 1000-(b.pm[1]*taille_case+taille_case), fill="blue")
    # i=0
    # def draw_next():
    #     global i
    #     if i < len(b.taches):
    #         for coord in b.taches[i].coordtask:
    #             canvas.create_rectangle(coord[0]*taille_case, 1000-coord[1]*taille_case, (coord[0]*taille_case + taille_case), 1000-(coord[1]*taille_case + taille_case), fill='red', outline='')
    #         i+=1
    #         canvas.after(1000,draw_next)
    # draw_next()

    # tk.mainloop()

    ####################
    # Partie d'Anthime #
    ####################

    #points de montage à vérifier
    target = [0,0]

    #génération de la grille remplie de zéros
    S.grid = [[0 for j in range (S.columns)] for i in range (S.lines)]
    points = [0,0,2,0]
    #Cibles a atteindre avecl'algorithme
    arm = Arm
    arm.taches = [[3,1],[3,0],[2,1]]
    arm.pm = [0,0]

    pointsGrid = apply_points_to_grid(S.grid, points)  # c'est la grille qui contient les positions de collisions
    S.nodeGrid = GenerateNodeGrid(pointsGrid)

    # print("Grille : 0=vide et 1=point de montage")
    # print(pointsGrid)

    #Donner à la fonction un Bras (Arm) et la fonction va modifier les parametres du bras en question pour lui donner la liste des mouvements
    pathfinding.CompleteArmTask(arm)
    print(arm.movements)
