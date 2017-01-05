#!/usr/bin/python3

from grid import *
import  random, socket, select, threading, sys



class Client (threading.Thread) :

    def __init__ (self, ip, port, socketClient, num):

        threading.Thread.__init__ (self)
        self.ip = ip
        self.port = port
        self.socketClient = socketClient
        self.num = num
        self.currentPlayer = -1
        

    def run (self) :

        print ("Connexion du joueur %s" % (self.num, ))
        grids = [grid(), grid(), grid()]
        currentPlayer = J1
        grids[J1].display ()
        sep = '\n'
        # Tour du joueur
        while grids[0].gameOver() == -1:
            if (currentPlayer == J1) :
                
                buf = ''
                while len(buf) < 4 :
                    buf += socketClient.recv (8)
                case = struct.unpack('!i', buf[:4])[0]
                if (grids[0].cells[case] == EMPTY) :
                    grids[0].play (num, case)
                    socketClient.send (bytes (OK))
                    currentPlayer = J2
                else :
                    socketClient.send (bytes (KO))
                    currentPlayer = J2
            
            else:
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
            print("You win !")
        else:
            print("you loose !")
        

    def checkCase (self, grid) :
        case = self.socketClient.recv (8192)
        if (grid.cells[case] == EMPTY) :
            grid.play (num, case)
            socketClient.send (bytes (OK))
            currentPlayer = J2
        else :
            socketClient.send (bytes (KO))
            currentPlayer = J2

    def setGrid (grid) :
        self.grid = grid

    def setCurrentPlayer (player) :
        self.currentPlayer = player
        
        
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind (( '', 1111))

#while (True) :
    
sock.listen (1)
print ("Lancement du serveur.")

    # Connexion joueur 1
(socketClient, (ip, port)) = sock.accept ()
joueur1 = Client (ip, port, socketClient, J1)
joueur1.start ()
    
    #(socketClient, (ip, port)) = sock.accept ()
    #joueur2 = Client (ip, port, socketClient, 2, grids[J2])
    #joueur2.start ()
