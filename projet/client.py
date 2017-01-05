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
sock.connect(("", 1111))
sep = '\n'

grid ()

while (True) :

    caseNumber = -1
    while caseNumber <0 or  caseNumber >= NB_CELLS:
        caseNumber = input ('Choisissez une case a jouer : ')
    caseNumber = pack ('!i', caseNumber)
    sock.send (caseNumber)

    buf = ''
    while len(buf) < 4 :
        buf += sock.recv (8)
    msg = struct.unpack('!i', buf[:4])[0]
    if (msg == OK) :
        grid.play (J1, caseNumber)
        grid.display ()
    else :
        grid.play (J2, caseNumber)
        grid.display ()
        print ("Tu t'es fait niké kek")
    
sock.close ()
