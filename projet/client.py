#!/usr/bin/python3

from grid import *
import  random, socket, select, threading, sys

print ("Bienvenue dans le jeu du morpion aveugle.")
print ("Pour jouer il suffit de choisir une case de 0 à 8, les cases sont numérotees de la maniere suivante :")
print ("")
print ("     0 1 2 ")
print ("     3 4 5 ")
print ("     6 7 8 ")
print ("")

# connexion au serveur
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 1111))
player = sock.recv (8192)
player = int(player)
grid = grid ()

while (True) :
    gameOver = sock.recv (8192)
    gameOver = int (gameOver)
    
    if(gameOver == 1):
        if grid.gameOver() == player:
            print("You win !")
        else:
            print("you loose !")
        break
    curentPlayer = sock.recv (8192)
    curentPlayer = int (curentPlayer)

    caseNumber = -1
    if (curentPlayer == player):
        while caseNumber <0 or  caseNumber >= NB_CELLS:
            caseNumber = input ('Choisissez une case a jouer : ')
            caseNumber = int (caseNumber)
        caseNumber = str (caseNumber)
        sock.send (caseNumber.encode ())
        caseNumber = int (caseNumber)
        msg = sock.recv (8192)
        msg = int (msg)
        if (msg == OK) :
            grid.play (J1, caseNumber)
            grid.display ()
        elif (msg == -1):
            print ("Tu a déjà joué cette case")
        else :
            grid.play (J2, caseNumber)
            grid.display ()
            print("Ton adversaire a déjà jouer cette case donc retente ta chance\n")
    else:
        print ("En attente du coup de l'autre joueur")


        
sock.close ()
