#!/usr/bin/python3

from grid import *
import  random, socket, select, threading, sys

grids = [grid(), grid(), grid()]
nb_players = 0

client_list = []
list_1 = []
list_2 = []
        
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0, None)
sock.bind (( '', 1111))
sock.listen (1)
        
while (True) :
    list_3 = select.select (client_list + [sock], list_1, list_2) [0]
    for i in list_3 :
        if (i == sock) : # Le client rejoint.
            nb_players += 1
            tmp_s = i.accept ()
            sock_addr = tmp_s [1]
            client_list += [tmp_s [0]]
            if (nb_players == 2):
                for j in client_list:
                    j.send (b"la partie va commencer")
            else:
                i.send (b"En attente d'un autre joueur")
                    
        else :
            data = i.recv (1500)
            if (len (data[0]) == 0) : # Le client part.
                client_list.remove (i)
                nb_players -= 1
            else :
                if (nb_players == 2):
                    print()
                else:
                    i.send(b"Pas assez de joueurs pour commencer à jouer")
                    

        



