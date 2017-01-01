#!/usr/bin/python3

from grid import *
import  random, socket, select, threading, sys

def main() :

    grids = [grid(), grid(), grid()]
    nb_players = 0
    
    # Partie serveur.
    if (sys.argv == 1) :
        
        client_list = []
        list_1 = []
        list_2 = []
        
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0, None)
        sock.bind (( '', 7777 ))
        sock.listen (1)
        
        while (True) :
            list_3 = select.select (client_list + [sock], list_1, list_2) [0]
            for i in list_3 :
                if (i == sock) : # Le client rejoint.
                    nb_players += 1
                    tmp_s = i.accept ()
                    sock_addr = tmp_s [1]
                    client_list += [tmp_s [0]]
                    i.send (bytes(nb_players))
                else :
                    data = i.recv (1500)
                    if (len (data[0]) == 0) : # Le client part.
                        client_list.remove (i)
                        nb_players -= 1
                    else :
                        print()
                    

    # Partie client.
    elif (sys.argv == 2) :
        server_name = sys.argv [1]
        
    
        
        current_player = J1
        grids[J1].display()
        while grids[0].gameOver() == -1 :
            if current_player == J1:
                shot = -1
                while shot <0 or shot >=NB_CELLS :
                    shot = int(input ("Quelle case allez-vous jouer ?"))
            else :
                shot = random.randint(0,8)
                while grids[current_player].cells[shot] != EMPTY:
                    shot = random.randint(0,8)
            if (grids[0].cells[shot] != EMPTY):
                grids[current_player].cells[shot] = grids[0].cells[shot]
            else:
                grids[current_player].cells[shot] = current_player
                grids[0].play(current_player, shot)
                current_player = current_player%2+1
            if current_player == J1:
                grids[J1].display()
        print("game over")
        grids[0].display()
        if grids[0].gameOver() == J1:
            print("You win!")
        else:
            print("you lose!")

main()
